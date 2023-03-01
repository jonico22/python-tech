from fabric import Connection, task

@task
def deploy(c:  Connection):
    print('>>> conectando al servidor remoto')
    print('>>> dirigiendo a la carpeta')
    with c.cd('python-tech'):
        print('>>> descargar los cambios')
        c.run('git pull origin main')
        with c.prefix('source env/bin/activate'):
            with c.prefix('export DATABASE_URI="postgresql://userdb:userdb@localhost:5432/flask_db"'):
                print('>>> actualizar los paquetes')
                c.run('pip3 install -r requirements.txt')
                print('>>> actualizar las tablas si es que hubiera un cambio')
                c.run('flask db upgrade')
    print('>>> resetear el servicio creado')
    c.sudo('systemctl restart flaskapp')
    print('>>> resetear el servidor')
    c.sudo('systemctl restart nginx')
    print('>>> deploy terminado')
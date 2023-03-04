# NOMBRE DEL PROYECTO: PYTHON TECH

## PRODUCCION

Se configuro un servidor en aws ec2 con las limitaciones de la capa gratuita.

La url del proyecto :

http://18.234.130.162/

La documentación se encuentra en la siguiente url :

http://18.234.130.162/swagger-ui

*este servidor es temporal hasta la evaluacion de la practica.

## DESARROLLADORES

Claudia González Fuentes

Jose Luis Yana Nicolas


# PASOS PREVIOS PARA EL ENTORNO DE TRABAJO

Si utiliza un entorno de windows con wsl2 o linux es recomendable actualizar los paquetes y seguir los siguientes pasos:

`sudo apt update`

Se recomienda verificar la version de python :

`python3 --version`

Si no tiene PIP (instalador de paquete) es necesario instalarlo :

`sudo apt install python3-pip`

## PREPARACION DE LA BASE DE DATOS (postgres)

Lo pasos para windows con wsl se recomiendo tener en cuenta este tutorial de microsoft

https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database

Luego de tener instalado la bd seguir los siguientes pasos :

Inicio sesion de Postgres con el siguiente comando:

`sudo -iu postgres psql`

Luego crea una base de datos para tu proyecto:

`CREATE DATABASE tech_db_dev;`

A continuación se debe crear un usuario de base de datos para nuestro proyecto:

`CREATE USER userdb WITH PASSWORD 'userdb'`

Luego dé a este nuevo acceso de usuario para administrar su nueva base de datos:

`GRANT ALL PRIVILEGES ON DATABASE tech_db_dev TO userdb;`

Para confirmar que se creó la base de datos :

`\l`

Para salir del Postgres :

`\q`

## INSTALACIÓN DEL PROYECTO

Clonar el repositorio , Dirigirte a la carpeta del repositorio

`git@github.com:jonico22/python-tech.git`

Luego iniciar el entorno

`python3 -m venv venv`

Luego activamos el entorno virtual

`source venv/bin/activate`

Despues comenzamos a  instalar las librerias que necesita :

`pip3 install -r requirements.txt`

Para iniciar el proyecto se debe crear un archivo .env con las  variables de entorno : 

`cp .env.example .env`

### INICIAR CON LA MIGRACION

En la misma carpeta del proyecto iniciar con el siguiente comando :

`flask db init`

Luego iniciar la migraciones :

`flask db migrate`

Actualizar las tablas :

`flask db upgrade`

Crear los registros(solamente una vez) con el siguiente comando :

`python3 init_db.py`

# INICIA EL PROYECTO

Despues de seguir los pasos previos , debe iniciar el servidor con el siguiente comando:

 `python3 app.py`

# TAREA PROGRAMADA

Para crear un tarea programada en este proyecto estamos utilizando fabric 3 y tambien estamos desplegando un servidor en AWS EC2 con una capa gratiuta y utilizamos el siguiente comando

`fab -i <key> deploy -H <servidor>`

# HERRAMIENTA Y LIBRERIAS UTILIZADAS 

Utilizamos la herramienta online gitignore.io para generar la configuracion de gitignore del proyecto , terminos usados son los siguientes:

flask,windows,macos,python

Esta son las librerias mas importantes :

```
Flask==2.2.3 -> la version mas actualizada
Flask-JWT-Extended==4.4.4 -> nos ayuda en la implementacion de seguridad para la aplicacion con tokens
Flask-Migrate==4.0.4 -> nos facilita la actualizacion de tablas
flask-smorest==0.40.0 -> nos ayuda para mejor implementacion de ruta y para la documentacion del proyecto
Flask-SQLAlchemy==3.0.3 -> ORM de la aplicacion
flask-cors -> Nos facilita Cors para las rutas
load_dotenv-> Obtener las variables de entorno se basa al modelo de NODE.js

# python-tech

utilizamos la herramienta online gitignore.io , terminos usados son

flask,windows,macos,python

Prueba realizada en entorno de windows con wsl2 - ubuntu

ingresar al entorno de ubuntu y actualizar la distribucion 

`sudo apt update`

verificar la version de python en este caso entorno wsl2 lo tiene con el nombre python3

`python3 --version`

tener instalado el instalador de paquetes pip

`sudo apt install python3-pip`

crear la carpeta de tu proyecto y luego crear el entorno virtual 

`python3 -m venv venv`

luego activamos el entorno virtual

`source venv/bin/activate`

desde ahi puedes comenzar instalar las librerias que necesita tu proyecto

si deseas guardar tus librerias que utilizas en archivo txt solo debes presionar el siguiente comando

`pip freeze > requirements.txt`

Los ambientes de desarrollo son :

main -> rama principal

develop -> rama de desarrollo

test -> rama de pruebas

Para iniciar el proyecto se debe utilizar variables de entorno por ejemplo :

export DATABASE_URI="postgresql://username:password@host:port/database_name"

# migrate

configurar la carpeta

flask db init

iniciar migraciones

flask db migrate

crear tablas

flask db upgrade


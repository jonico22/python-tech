import os
from dotenv import load_dotenv
import psycopg2
from werkzeug.security import generate_password_hash
load_dotenv()
conn = psycopg2.connect(
        host="localhost",
        database= os.getenv('DB_NAME'),
        user= os.getenv('DB_USER'),
        password=os.getenv('DB_PASS') )

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the table rol
cur.execute("INSERT INTO ROLES(NAME,STATUS) VALUES ('admin',true)")

# Insert data into the table paises
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Argentina', 'ARG', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Bolivia', 'BOL', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Chile', 'CHL', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Colombia', 'COL', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Costa Rica', 'CRI', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Ecuador', 'ECU', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('México', 'MEX', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Paraguay', 'PRY', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Panamá', 'PAN', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Perú', 'PER', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Puerto Rico', 'PRI', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('República Dominicana', 'DOM', true)")
cur.execute("INSERT INTO PAISES(NAME, CODE ,STATUS) VALUES ('Uruguay', 'URY', true)")

# Insert data into the table categorias
cur.execute("INSERT INTO CATEGORIAS(NAME,STATUS) VALUES ('Seguridad',true)")
cur.execute("INSERT INTO CATEGORIAS(NAME,STATUS) VALUES ('Transporte',true)")
cur.execute("INSERT INTO CATEGORIAS(NAME,STATUS) VALUES ('Hospedaje',true)")
cur.execute("INSERT INTO CATEGORIAS(NAME,STATUS) VALUES ('Turismo ',true)")
cur.execute("INSERT INTO CATEGORIAS(NAME,STATUS) VALUES ('Clima ',true)")
cur.execute("INSERT INTO CATEGORIAS(NAME,STATUS) VALUES ('Comida',true)")


# Insert data into the table user
cur.execute('INSERT INTO USERS (USERNAME,EMAIL,PASSWORD,ROL_ID,STATUS)'
            'VALUES (%s, %s, %s, %s,%s)',
            ('superadmin',
             'superadmin@gmail.com',
             generate_password_hash('12345678',method="sha256"),
             1,
             True)
            )

conn.commit()

cur.close()
conn.close()
print('se creo los registros')


import os
import psycopg2
from werkzeug.security import generate_password_hash

conn = psycopg2.connect(
        host="localhost",
        database="tech_db_dev",
        user='userdb',
        password='userdb')

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert data into the table rol
cur.execute("INSERT INTO ROLES(NAME,STATUS) VALUES ('admin',true)")

# Insert data into the table user
cur.execute('INSERT INTO USERS (USERNAME,EMAIL,PASSWORD,ROL_ID,STATUS)'
            'VALUES (%s, %s, %s, %s,%s)',
            ('superadmin',
             'superadmin@gmail',
             generate_password_hash('12345678',method="sha256"),
             1,
             True)
            )

conn.commit()

cur.close()
conn.close()
print('se creo los registros')


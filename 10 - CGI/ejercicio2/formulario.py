#!C:\Program Files\Python312\python.exe

import cgi
import hashlib
import mysql.connector

print("Content-type: text/html\n")
print("<html><head><title>Formulario Procesado</title></head><body>")
form = cgi.FieldStorage()

nombre = form.getvalue('nombre', '')
email = form.getvalue('email', '')
passwd = form.getvalue('passwd', '')

if nombre and email and passwd:
    # Database connection
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cgi_bbdd',
            user='root',
            password='')
        
        cursor = connection.cursor()

        # Convert the password to bytes
        passwd_bytes = passwd.encode('utf-8')

        # Create an SHA-256 hash object
        passwd_hash = hashlib.sha256()

        # Update the hash with the password bytes
        passwd_hash.update(passwd_bytes)

        # Get the hexadecimal representation of the hash
        passwd_hash_hex = passwd_hash.hexdigest()

        # Insert data into the database using a parameterized query
        query = "INSERT INTO usuarios (nombre, correo, passwd) VALUES (%s, %s, %s)"
        data = (nombre, email, passwd_hash_hex)
        cursor.execute(query, data)

        # Commit the changes to the database
        connection.commit()

        print("<h2>Registro exitoso</h2>")
    except mysql.connector.Error as err:
        print("<h2>Error en la base de datos: {}</h2>".format(err))
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print("<h2>Faltan datos en el formulario.</h2>")

print("</body></html>")

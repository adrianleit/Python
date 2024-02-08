import mysql.connector
import hashlib

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba')

cursor = connection.cursor()

eleccion=int(input('Pulse 1: si quieres crear un usuario, Pulse 2: si desea modificar el nombre de usuario'))

if eleccion == 1:
    #Crear usuario
    usuario=input('Dime tu nickname: ')
    correo=input('Dime tu email: ')
    passwd=input('Dime tu password: ')

    # Convertir la contraseña a bytes
    passwd=passwd.encode('utf-8')
    
    # Crear un objeto hash SHA-256
    passwd_sec=hashlib.sha256()

    # Actualizar el hash con los bytes de la contraseña
    passwd_sec.update(passwd)

    # Obtener la representación hexadecimal del hash
    passwd_sec=passwd_sec.hexdigest()

    cursor.execute("INSERT INTO usuarios (nickname, correo, passwd) VALUES ('"+usuario+"','"+correo+"','"+passwd_sec+"');")
elif eleccion == 2:
    correo=input('Dime tu correo: ')
    usuario_nuevo=input('Dime tu nuevo nickname: ')
    cursor.execute("UPDATE usuarios SET nickname='"+usuario_nuevo+"' WHERE correo='"+correo+"';")


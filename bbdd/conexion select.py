import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='clinica2023',
    user='root',
    password='')

cursor = connection.cursor()
cursor.execute("select * from pacientes")
pacientes = cursor.fetchall()

for paciente in pacientes:
    print (paciente)
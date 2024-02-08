import mysql.connector
#Conexion a la bbdd

def conexion_bbdd(bbdd):
    connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database=bbdd)

#!C:\Program Files\Python312\python.exe

import cgi

print("Content-type: text/html\n")
print("<html><head><title>Formulario Procesado</title></head><body>")
form = cgi.FieldStorage()
if "nombre" in form:
    nombre = form["nombre"].value
    print("<h2>Hola, {}</h2>".format(nombre))
else:
    print("<h2>No se proporcionó un nombre.</h2>")
print("</body></html>")

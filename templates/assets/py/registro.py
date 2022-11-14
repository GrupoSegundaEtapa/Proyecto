#!C:\Python27\python.exe
import mysql.connector
import cgi
print "Content-type: text/html\n\n";
form = cgi.FieldStorage()

user = form.getvalue("user")

print(user)

# try:
#     conexion = mysql.connector.connect(host='localhost', database='academia', user='root', password='')
#     if conexion.is_connected():
#             db_Info=conexion.get_server_info()
#             print("Conectado al servidor MySQL Version: ", db_Info)
#             cursor=conexion.cursor()
#             cursor.execute("select database();")
#             record=cursor.fetchone()
#             print("Se ha conectado a la base de datos: ", record)
# except mysql.connector.Error as error:
#     print("error en la conexion ", error)
# finally:
#     if conexion.is_connected():
#         cursor.close()
#         conexion.close()
#         print("Conexion cerrada")
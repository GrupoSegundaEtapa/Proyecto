#!C:\Python27\python.exe
import mysql.connector
import cgi
print("Content-type: text/html\n\n")
form = cgi.FieldStorage()

user = form.getvalue('user')
email = form.getvalue('email')
passw = form.getvalue('password')

try:
 connection = mysql.connector.connect(host='localhost',
 database='academia',
 user='root',
 password='')
 mySql_insert_query = """INSERT INTO usuarios ( nombre_user, email_user, pass_user)
 VALUES (%s, %s, %s, %s) """
 records_to_insert = [( user, email, passw)]
 cursor = connection.cursor()
 cursor.executemany(mySql_insert_query, records_to_insert)
 connection.commit()
 print(cursor.rowcount, "Record inserted successfully into products table")
except mysql.connector.Error as error:
 print("Failed to insert record into MySQL table {}".format(error))
finally:
 if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")









# #!C:\Python27\python.exe
# import mysql.connector
# import cgi
# print "Content-type: text/html\n\n";
# form = cgi.FieldStorage()

# user = form.getvalue("user")

# print(user)

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
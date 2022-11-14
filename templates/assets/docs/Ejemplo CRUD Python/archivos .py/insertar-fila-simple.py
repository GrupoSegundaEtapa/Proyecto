import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python-db',
                                         user='root',
                                         password='mariano')

    mySql_insert_query = """INSERT INTO productos (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (001, 'Lenovo ThinkPad P71', 25000, '2021-05-18') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into products table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

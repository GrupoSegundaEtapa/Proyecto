from datetime import datetime

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python-db',
                                         user='root',
                                         password='mariano')

    mySql_insert_query = """INSERT INTO productos (Id, Name, Price, Purchase_date) 
                            VALUES (%s, %s, %s, %s) """

    cursor = connection.cursor()
    current_Date = datetime.now()
    # convert date in the format you want
    formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
    insert_tuple = (7, 'Acer Predator Triton', 2435, current_Date)

    result = cursor.execute(mySql_insert_query, insert_tuple)
    connection.commit()
    print("Date Record inserted successfully")

except mysql.connector.Error as error:
    connection.rollback()
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

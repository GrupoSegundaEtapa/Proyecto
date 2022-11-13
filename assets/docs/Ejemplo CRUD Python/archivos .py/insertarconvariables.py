import mysql.connector

def insert_varibles_into_table(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python-db',
                                             user='root',
                                             password='mariano')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO productos (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        record = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into products table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

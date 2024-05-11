import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_db_connection():
    
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None





"""def delete_query(connection, query):
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("rows deleted")
    except Error as e:
        print(f"The error '{e}' occured")"""




def rename_table(connection, query):

    mycursor = connection.cursor() 
    try:
        mycursor.execute(query) 
    except Error as e:
        print(f"The error '{e}' occured")
        


def rename_column(connection,query):
    mycursor= connection.cursor()
    try:
        mycursor.execute(query)
    except Error as e:
        print(f"The error '{e}' occured")


"""if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        query ="ALTER TABLE authors RENAME to reporters"
        update_query = rename_table(conn,query)
        print("updated table name", update_query)"""


if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        query ="ALTER TABLE news RENAME COLUMN editor_id TO publisher_id;"
        update_query = rename_column(conn,query)
        print("updated", update_query)
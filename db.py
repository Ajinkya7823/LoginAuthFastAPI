import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # change to your MySQL user
        password="a7823", # change to your MySQL password
        database="simpledb"  # make sure this database exists
    )

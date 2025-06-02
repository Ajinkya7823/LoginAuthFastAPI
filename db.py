import pymysql
from fastapi import HTTPException

def get_connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='a7823',
            database='simpledb',
            cursorclass=pymysql.cursors.DictCursor,  # optional: rows dict स्वरूपात येतील
            charset='utf8mb4'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

import pyodbc

def connect():
    # Connect to SQL Server
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=;'
                        'DATABASE=;'
                        'UID=;'
                        'PWD=')
    
    return conn

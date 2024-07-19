import pyodbc

def connect():
    # Connect to SQL Server
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=ATPWEBDBN1;'
                        'DATABASE=dbWorkFlow;'
                        'UID=wfWI;'
                        'PWD=ATPWI2018!')
    
    return conn
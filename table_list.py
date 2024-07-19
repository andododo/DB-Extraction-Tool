import pyodbc
import db_connection

def fetch():

    conn = db_connection.connect()

    # Create a cursor object
    cursor = conn.cursor()

    # Query to get the list of tables
    query = """
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE = 'BASE TABLE'
    AND TABLE_CATALOG = ?
    AND TABLE_SCHEMA = 'dbo'
    ORDER BY TABLE_NAME
    """

    # Execute the query
    cursor.execute(query, (conn.getinfo(pyodbc.SQL_DATABASE_NAME)))

    # Fetch all table names
    tables = cursor.fetchall()

    # Display the list of tables
    print("List of tables in the database:")
    for i, table in enumerate(tables, start=1):
        table_name = table[0]
        print(f"[{i}] {table_name}")
    
    # Prompt the user to enter the table number
    table_number = int(input("Enter the number of the table you want to query: "))

    # Retrieve the table name from the list based on the entered number
    selected_table_name = tables[table_number - 1][0]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return selected_table_name
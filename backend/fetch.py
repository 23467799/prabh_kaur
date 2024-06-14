import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
            
            dbname='myappdb',
            user='myuser',
            password='mypassword',
            host='130.211.114.90',
            port='5432',
        )
    
    print("Connection to the database established successfully.")
except Exception as e:
    print(f"Error: {e}")

# Query to execute
query = "SELECT * FROM  mytable;"

# Execute the query and fetch the data
try:
    df = pd.read_sql_query(query, conn)
    print("Query executed successfully.")
except Exception as e:
    print(f"Error: {e}")

# Display the data in a table format
print(df)

# Close the database connection
conn.close()
print("Database connection closed.")
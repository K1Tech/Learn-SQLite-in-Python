# 0. import required lib
import sqlite3
import pandas as pd

# 1. define connection
conn = sqlite3.connect(r'D:\Code\py\4-Database\smalldata.db')

# 2. define query
query = "SELECT * FROM table1"

df = pd.read_sql_query(query, conn)
df.to_csv(r'D:\Code\py\4-Database\output\out.csv', index=False)
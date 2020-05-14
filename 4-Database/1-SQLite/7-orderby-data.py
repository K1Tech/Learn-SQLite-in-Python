# 0. import required lib
import sqlite3
#import pandas

# 1. define connection
conn = sqlite3.connect(r'D:\Code\py\4-Database\smalldata.db')

# 2. define cursor method
c = conn.cursor()

# 3. define query
query = "SELECT * FROM `table1` ORDER BY count"

# 3. execute query
c.execute(query)

# 4. fetch rows
rows = c.fetchall()

# 5. print rows
print(rows)

# 6. using pandas
#df = pandas.read_sql_query(query, conn)
#print(df)
# 0. import required lib
import sqlite3

# 1. define connection
conn = sqlite3.connect(r'D:\Code\py\4-Database\smalldata.db')

# 2. define cursor method
c = conn.cursor()

# 3. define query
create_table = """ CREATE TABLE IF NOT EXISTS table1 (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    year,
                    age,
                    ethnic,
                    sex,
                    area,
                    count
                ); """

# 3. execute query
c.execute(create_table)
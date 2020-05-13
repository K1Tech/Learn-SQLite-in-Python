# 0. import required lib
import sqlite3

# 1. define connection
conn = sqlite3.connect(r'D:\Code\py\4-Database\smalldata.db')

# 2. define cursor method
c = conn.cursor()

# 3. define query
insert_query = """ INSERT INTO table1 (year,age,ethnic,sex,area,count)
                    VALUES  (2018,0,1,1,1,795),
                            (2018,0,1,1,2,5067); """

# 3. execute query
c.execute(insert_query)

# 4. commit changes
c.execute("commit")
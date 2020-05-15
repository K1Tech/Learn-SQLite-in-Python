# 0. import required lib
import sqlite3
import pandas as pd

# 1. define connection
conn = sqlite3.connect(r'D:\Code\py\4-Database\smalldata.db')

# 2. define cursor method
c = conn.cursor()

# 3. execute begin transaction 
c.execute("begin")

# 4. defining variables
year = 2017
age = 123
ethnic = 1
sex = 1
area = 12
count = 10000

# 5. executing sql 
c.execute("INSERT INTO table1 (year,age,ethnic,sex,area,count) VALUES ("+ year+","+ age+","+ ethnic+","+ sex+","+ area+","+ count+")")

# 6. commit the transaction
c.execute("commit")

# 7. reading data by pandas
df = pd.read_sql_query("select * from table1 where age = 123", conn)
print(df)
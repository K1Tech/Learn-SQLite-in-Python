# 0. import required lib
import sqlite3
from sqlite3 import Error
import csv

# 1. opening csv file
with open (r'd:\Code\py\4-Database\output\smalldata.csv','r') as infile:
    
    # 2. define content by delimiter
    content = csv.DictReader(infile, delimiter=',')

    # 3. define connection
    conn = sqlite3.connect(r'D:\Code\py\4-Database\smalldata.db')

    # 4. define cursor method
    c = conn.cursor()

    # 5. execute begin transaction 
    c.execute("begin")

    # 6. using try for avoiding exceptions
    try:

        # 7. reading csv line by line
        for line in content:

            # 8. defining each data in a line
            year = line['Year']
            age = line['Age']
            ethnic = line['Ethnic']
            sex = line['Sex']
            area= line['Area']
            count= line['count']

            # 9. executing insert query
            c.execute(""" INSERT INTO table1 (year,age,ethnic,sex,area,count)
              VALUES (:year, :age, :ethnic, :sex, :area, :count)""",\
                        {'year':year, 'age':age, 'ethnic':ethnic, 'sex':sex, 'area':area, 'count':count})
            # 10. commit the transaction
            c.execute("commit")

    # 11. defining the exception
    except Error:
        print("failed!")

        # 12. executing rollback in case of an exception
        c.execute("rollback")
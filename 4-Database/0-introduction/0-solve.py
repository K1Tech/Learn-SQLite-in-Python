#%%
import sqlite3
from sqlite3 import Error
import csv
import numpy as np
import pandas as pd


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def ddl_query(conn, ddl_query_sql):
    try:
        c = conn.cursor()
        c.execute(ddl_query_sql)
    except Error as e:
        print(e)

def import_csv(db):        
    with open (r'd:\Code\py\4-Database\output\smalldata.csv','r') as infile, db:
        content = csv.DictReader(infile, delimiter=',')  # csv generator to the file, will be read line by line

        cursor = db.cursor()
        cursor.execute("begin")
        try:
            for line in content:
                # line is a dict, where each column name is the key
                # no need to sanitize the header row, that was done automatically upon reading the file
                year = line['Year']
                age = line['Age']
                ethnic = line['Ethnic']
                sex = line['Sex']
                area= line['Area']
                count= line['count']
                cursor.execute('''INSERT INTO table1 (year,age,ethnic,sex,area,count) VALUES (:year, :age, :ethnic, :sex, :area, :count)''',\
                        {'year':year, 'age':age, 'ethnic':ethnic, 'sex':sex, 'area':area, 'count':count})
                cursor.execute("commit")
        except Error:
            print("failed!")
            cursor.execute("rollback")


    # no file closing, that is automatically done by 'with open()'
    # no db close or commit - the DB connection is in a context manger, that'll be done automatically (the commit - if there are no exceptions)

def read_first_100(conn):
    sql_select_first_100 = """ select * from table1 limit 100;"""
    df = pd.read_sql_query(sql_select_first_100, conn)
    print(df)


def main():
    database = r'd:\Code\py\4-Database\datasets\db\bigdata1.db'

    sql_drop_table = 'DROP TABLE IF EXISTS table1'
    sql_create_table = """ CREATE TABLE IF NOT EXISTS table1 (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        year text,
                                        age text,
                                        ethnic text,
                                        sex text,
                                        area text,
                                        count text
                                    ); """
    
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        ddl_query(conn, sql_drop_table)
        ddl_query(conn, sql_create_table)
        import_csv(conn)
        read_first_100(conn)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
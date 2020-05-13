# %%
import sqlite3
import pandas

conn = sqlite3.connect(r"d:\Code\py\4-Database\datasets\db\example.db")
df = pandas.read_sql_query('SELECT * FROM `HighScores`', conn,index_col='id')
print(df)
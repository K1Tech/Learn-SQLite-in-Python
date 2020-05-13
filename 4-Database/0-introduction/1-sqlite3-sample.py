# %%
import sqlite3

conn = sqlite3.connect(r"d:\Code\py\4-Database\datasets\db\example.db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM `HighScores`')
rows = cursor.fetchall()
print('High Scores:', rows)
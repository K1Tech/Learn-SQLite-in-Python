# %%
from databases import Database

database = Database(r'sqlite:///d:\Code\py\4-Database\datasets\db\example.db')
await database.connect()
rows = await database.fetch_all(query='SELECT * FROM `HighScores`')
print('High Scores:', rows)


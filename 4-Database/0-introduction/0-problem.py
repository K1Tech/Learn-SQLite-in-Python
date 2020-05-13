import numpy as np
import pandas as pd


csv_base_dir = r"d:\Code\py\4-Database\datasets\csv"
# %%
sample1 = pd.read_csv(csv_base_dir + '\sample1.csv')
#sample1.head()
sample1

# %%
(sample1.assign(Lat=lambda x: x.latitude,
            Long=lambda x: x.longitude)
    .plot(kind='scatter', x='Lat', y='Long'))


# %%
sampleData = pd.read_csv(csv_base_dir + r'\bigdata.csv')
sampleData.head()

# %%
# Open by MS Excel
import os
os.system(r'C:\"Program Files"\"Microsoft Office"\root\Office16\excel  d:\Code\py\4-Database\datasets\csv\bigdata.csv')

# Excel limitation:
#https://www.google.com/search?q=excel+row+limit


# %%
# Open by Notepad
import os
os.system(r'notepad d:\Code\py\4-Database\datasets\csv\bigdata.csv')

# Creating a small file:
# Get-Content d:\Code\py\4-Database\datasets\csv\bigdata.csv -Encoding byte -TotalCount 2KB | Set-Content d:\Code\py\4-Database\output\smalldata.csv -Encoding byte

# %%
# Read bigdata by using pandas
big_data = pd.read_csv(csv_base_dir + r'\bigdata.csv', nrows=10)
big_data

# %%

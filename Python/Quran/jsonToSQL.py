import pandas as pd
import json
import sqlite3

# Open JSON data in UTF-8 as file has arabic
with open("C:\\Users\\sunrise\\Documents\\Kasim\\Submission\\Python\\Quran\\surah2.json", encoding="utf8") as f:
    data = json.load(f)

# Create A DataFrame From the JSON Data
df = pd.DataFrame(data)


conn = sqlite3.connect('C:\\Users\\sunrise\\Documents\\Kasim\\Submission\\Python\\Quran\\surah.sqlite')
c = conn.cursor()

# convert dataframe to SQL
df.to_sql("surah",conn)

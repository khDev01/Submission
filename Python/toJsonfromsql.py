import sqlite3
import json
import pandas as pd
from pandas import DataFrame
import numpy as np

db_file = r"C:\Users\sunrise\Documents\Kasim\Submission\MedinaArabic\MedinaArabicAll.sqlite"
save_json=  r"C:\Users\sunrise\Documents\Kasim\Submission\MedinaArabic\lesson3.json"

# save_json =  r"C:\Users\sunrise\code\template\src\lesson1.json"

# save_json =  r"C:\Users\sunrise\github\react-flashcards\react-flashcard\src\book1.json"

conn = sqlite3.connect(db_file)
cur = conn.cursor()
query = "SELECT * FROM BOOK3"

data = pd.read_sql(query, conn)
data['English'] = data['English'].str.capitalize()
df = DataFrame(data, columns= ['id','Lesson', 'English', 'Arabic'])
# add unique identifier
df['id'] = np.arange(df.shape[0])
df.to_json(save_json, orient='records')
print(df)

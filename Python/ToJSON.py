import sqlite3
from pandas import DataFrame
import requests
import pandas as pd
import numpy as np

columnNo = []
columnA = []
columnB = []

# book 1 has 23 lessons
test = True
maxLessons = 24
if test == True:
    maxLessons = 3

for x in range(1, maxLessons):
    url = 'https://app.memrise.com/course/298802/madina-arabic-book-1-2/' + str(x) + '/'
    response = requests.get(url, timeout=5)
    # print(response.status_code) # 200 OK page is present
    soup = BeautifulSoup(response.content, "html.parser")

    cola = soup.select(".col_a > .text")
    for rows in cola:
        # print (rows.text)
        columnA.append(rows.text)
        columnNo.append(x)

    colb = soup.select(".col_b > .text")
    for rows in colb:
        columnB.append(rows.text)

conn = sqlite3.connect('Documents\\Kasim\\Submission\\MedinaArabic\\testdb.sqlite')
c = conn.cursor()

c.execute('CREATE TABLE BOOK1 (Lesson, English, Arabic)')
conn.commit()

book1 = {'Lesson':columnNo,
        'English':columnA,
        'Arabic':columnB
        }

df = DataFrame(book1, columns= ['Lesson', 'English', 'Arabic'])
df.to_sql('BOOK1', conn, if_exists='replace', index = False)

c.execute('''
SELECT * FROM Book1
          ''')

# for row in c.fetchall():
#     print (row)

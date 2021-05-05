from bs4 import BeautifulSoup
import requests
import json
import os

url = 'https://atom.io/'
response = requests.get(url, timeout=5)
# print(response.status_code) # 200 OK page is present

soup = BeautifulSoup(response.content, "html.parser")

featureArr = []
for features in soup.find_all('h4'):
    print(features.text)
    # get current directory to create path for outfile as below L22
    print(os.getcwd())
    featureObj = {
        "feature": features.text
    }
    featureArr.append(featureObj)

with open('Documents\\ProjectFolder\\featureData.json', 'w') as outfile:
    json.dump(featureArr, outfile)





cola = soup.select(".col_a > .text")
for rows in cola:
    # print (rows.text)
    columnA.append(rows.text)

colb = soup.select(".col_b > .text")
for rows in colb:
    # print (rows.text)
    columnB.append(rows.text)

listToStr = ' '.join(map(str, columnA))
print (listToStr)



=========================================
cola = soup.select(".col_a > .text")
for rows in cola:
    # print (rows.text)
    columnA.append(rows)

print (columnA)
with open('Documents\\Kasim\\MedinaArabic\\Data.csv', 'w') as work:
    data = ["Words"]
    z = csv.writer(work)
    z.writerow(data)
    z.writerows(columnA)

============================================
import sqlite3
from pandas import DataFrame
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

columnNo = []
columnA = []
columnB = []

# book 1 has 23 lessons
for x in range(1, 24):
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

conn = sqlite3.connect('Documents\\Kasim\\MedinaArabic\\MedinaArabic1.db')
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

for row in c.fetchall():
    print (row)
    =================================================================

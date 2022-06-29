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
for x in range(1, 3):
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

df = pd.DataFrame({'Lesson':columnNo,
                   'English':columnA,
                   'Arabic':columnB})
writer = ExcelWriter('C:\\Users\\sunrise\\Desktop\\test1.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
# input()
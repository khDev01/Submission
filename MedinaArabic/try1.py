from bs4 import BeautifulSoup
import requests
import json
import csv

url = 'https://app.memrise.com/course/298802/madina-arabic-book-1-2/1/'
response = requests.get(url, timeout=5)
# print(response.status_code) # 200 OK page is present

soup = BeautifulSoup(response.content, "html.parser")

columnA = []
columnB = []
# for rows in soup.find_all('col_a col text'):
# #     print(features.text)
#     columnA.append(rows)
#     featureObj = {
#         "feature": features.text
#     }
#     featureArr.append(featureObj)

cola = soup.select(".col_a > .text")
colb = soup.select(".col_b > .text")
for rows in cola:
    # print (rows.text)
    columnA.append(rows.text)
    # i = 0
for rows in colb:
    columnB.append(rows.text)
#     i = i + 1
# listToStr = ' '.join(map(str, columnA))
# print (listToStr)

# with open('Documents\\Kasim\\MedinaArabic\\Data.html', 'w') as outfile:
#     outfile.write(convertedStr)

# print (columnA)
# with open('Documents\\Kasim\\MedinaArabic\\Data.csv', 'w') as work:
#     data = ["Words"]
#     z = csv.writer(work)
#     z.writerow(data)
#     z.writerows(columnA)


# with open('Documents\\Kasim\\MedinaArabic\\Data.csv','r') as csvinput:
#     with open('Documents\\Kasim\\MedinaArabic\\output_1.csv', 'w') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(csvinput)
#         all = []
#         row = next(reader)
#         row.append('Berry')
#         all.append(row)
#         for row in reader:
#             row.append(row[0])
#             all.append(row)
#         writer.writerows(all)

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
# csv_input = pd.read_csv('Documents\\Kasim\\MedinaArabic\\Data.csv')
# csv_input['Berries'] = csv_input['Words']
# csv_input.to_csv('Documents\\Kasim\\MedinaArabic\\output_1.csv', index=False)

df = pd.DataFrame({'English':columnA,
                   'Arabic':columnB})
writer = ExcelWriter('Documents\\Kasim\\MedinaArabic\\Pand7as-Example.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

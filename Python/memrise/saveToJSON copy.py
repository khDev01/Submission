from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pandas import DataFrame

columnNo = []
columnA = []
columnB = []
mydata = {}

# book 1 has 23 lessons
test = False
maxLessons = 24
if test == True:
    maxLessons = 3

for x in range(1, maxLessons):
    url = 'https://app.memrise.com/course/54796/medina-arabic-book-1-no-typing/' + str(x) + '/'
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

res = {}
# Arabic/english array only
for key in columnA:
    for value in columnB:
        res[key] = value
        columnB.remove(value)
        break  
  
save_json=  r"C:\Users\sunrise\Documents\Kasim\Submission\Python\data\toJsontest2.json"
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))
with open(save_json, 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=8, ensure_ascii=False)

# for row in c.fetchall():
#     print (row)

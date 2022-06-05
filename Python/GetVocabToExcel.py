from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import ExcelWriter

columnNo = []
columnA= []
columnB = []
courseurl = 'https://app.memrise.com/course/NO/COURSENAME/'
output = 'C:\\Users\\sunrise\\Documents\\Kasim\\Submission\\Python\\data\\myfile.xlsx'
lessonCount = 1
url = courseurl

test = True
if test == True:
    print('Test')
    lessonCount = 10
else: # Get lesson count
    response = requests.get(url, timeout=5)
    print(response.status_code) # 200 OK page is present
    soup = BeautifulSoup(response.content, "html.parser")
    lessonCount = len(soup.find_all(class_="level"))
    lessonCount += 1
    # print(lessonCount)

# Get data from app.memrise.com
for x in range(1, lessonCount):
    url = courseurl + str(x) + '/'
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

print('Converting data')
# convert to excel
df = pd.DataFrame({'Lesson':columnNo,
                   'English':columnA,
                   'Arabic':columnB})
writer = ExcelWriter(output)
df.to_excel(writer,'Sheet1',index=False)
writer.save()
print('Saved file')

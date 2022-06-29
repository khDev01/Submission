from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pandas import DataFrame

columnNo = []
columnA = []
columnB = []
lessonCount = 1
courseurl = 'https://app.memrise.com/course/54796/medina-arabic-book-1-no-typing/'
url = courseurl
save_json=  r"C:\Users\sunrise\Documents\Kasim\Submission\Python\data\book1vocabV2.json"


test = False
if test == True:
    print('Test')
    lessonCount = 3
else: # Get lesson count
    response = requests.get(url, timeout=5)
    print(response.status_code) # 200 OK page is present
    soup = BeautifulSoup(response.content, "html.parser")
    lessonCount = len(soup.find_all(class_="level"))
    lessonCount += 1
    print(lessonCount)

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

# res = {}
# # Arabic/english array only
# for key in columnA:
#     for value in columnB:
#         res[key] = value
#         columnB.remove(value)
#         break  


df = pd.DataFrame({#'L':columnNo,
                   'En':columnB,
                   'Ar':columnA,
                   'M':True,
                   #'T':'' 
                   })


# df = pd.DataFrame({'L':columnNo,
#                    'En':columnB,
#                    'Ar':columnA,
#                    'M':True,
#                    'T':''})


# save_json=  r"C:\Users\sunrise\Documents\Kasim\Submission\Python\data\toJsontest4a.json"
# df = pd.DataFrame({#'L':columnNo,
#                    'En':columnB,
#                    'Ar':columnA,
#                    'M':True,
#                    'T':''
#                    }, index=columnB)

# save_json=  r"C:\Users\sunrise\Documents\Kasim\Submission\Python\data\toJsontest5.json"
# df = pd.DataFrame({#'L':columnNo,
#                    'En':columnB,
#                    'Ar':columnA,
#                    },)


# saves code with unicode chars (no 'escaping')
with open(save_json, 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False, orient='records')
print('saved file')
# df.to_json(save_json, orient='records')


  


# Printing resultant dictionary 
# print ("Resultant dictionary is : " +  str(res))
# with open(save_json, 'w', encoding='utf-8') as f:
#     json.dump(res, f, indent=8, ensure_ascii=False)

# for row in c.fetchall():
#     print (row)

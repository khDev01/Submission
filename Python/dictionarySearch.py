from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pandas import DataFrame

columnNo = []
columnA = []
columnB = []
url = 'https://www.livingarabic.com/en/search?q=%D9%81%D9%8E%D9%85%D9%8C&dc%5B%5D=1&st%5B%5D=0&st%5B%5D=1&st%5B%5D=2&new_google_recaptcha_token=03AGdBq27p4KPVu2wqbASoUFlRYj9M6XD6MmKoRM5U059R6mmAkIYdVkHbT1vs0yEY8LKQ-Q62eGxEaRXjsP8qAuWDGI9tGsQXZ1R5hK0zU7usNiERSZM54F1gsR-6omtUsuyWDD2tfJAh0gwTjxWTBK37Fka0-obXG1WNkWaDSur20Nuw4RX1o8qJz8EgnWb1AY7gkhSChKRPAF8B--7mgTt56LEM7W86tL8P-Lu8ZOA8vqMJ2ff8EQDgfOQZvdrQLlYzd-fa4nU6rj4ZfxjLY6lym7e9fh652WTYBnMVLJLusV0MwCVGk-GYnoX7XMC-2ff7by8mgG8CeqC49Cp588V0J9iE_WJURPF--o1GVFYlMO4qkIbAsiedN4BPGJS2gFJCHaMIR4fgUucS4_FVgwu_Xw0q6VPbj8E1ZyJOtrO1SO4EBYaNfE2VIfc8PJHrGFMAtzByGmAkjRNy4Yhvi6E85N_GywW0U2oDC2bh55AieCwatMUos4g'
save_json=  r"C:\Users\sunrise\Documents\Kasim\Submission\Python\mytest.json"

test = True
if test == True:
    print('Test')
    response = requests.get(url, timeout=5)
    # print(response.status_code) # 200 OK page is present
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    with open(save_json, "a") as o:
        o.write(soup)

    # cola = soup.select(".col_a > .text")
    # for rows in cola:
    #     # print (rows.text)
    #     columnA.append(rows.text)
    #     columnNo.append(x)

    # colb = soup.select(".col_b > .text")
    # for rows in colb:
    #     columnB.append(rows.text)

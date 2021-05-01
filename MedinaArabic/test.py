import sqlite3
from pandas import DataFrame
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import random

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_lesson_6(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK1 WHERE Lesson=6")

    rows = cur.fetchall()
    random.shuffle(rows)
    print(rows[0][1] + rows[0][2])
    print("No of words:"+ len(rows))
    print("")
    print(rows[-4:])

    for row in rows[-4:]:
        print(row[1] + row[2])
    print("")
    # listToStr = ' '.join(map(str, rows))
    # print (listToStr)
    # state encoding {encoding='utf-8'} for arabic
    # with open('Documents\\Kasim\\MedinaArabic\\Data.html', 'w', encoding='utf-8') as outfile:
    #     outfile.write(listToStr)

    for row in rows:
        print(row[1])


def main():
    database = r"C:\Users\sunrise\Documents\Kasim\MedinaArabic\MedinaArabic1.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Query lesson 6")
        select_lesson_6(conn)

if __name__ == '__main__':
    main()

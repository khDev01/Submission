import sqlite3 as lite
import sys

con = lite.connect(r'C:\Users\sunrise\Documents\Kasim\Submission\Python\population.odb')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537)")
    cur.execute("INSERT INTO Population VALUES(NULL,'France', 66415161)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")

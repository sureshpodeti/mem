import sqlite3
import time
import datetime
import os
import sys
from progressive.bar import Bar



def process_request(obj):
 _amount = obj.amount
 _tag = obj.tag
 _year = datetime.datetime.today().strftime("%Y")
 _month = datetime.datetime.today().strftime("%B")
 _day = datetime.datetime.now().strftime("%d")

 # create a database of for the current year
 path = os.path.join(os.path.dirname(__file__,), '..', '..', 'data', _year+'.db')
 conn = sqlite3.connect(path) 
 
 # create a table for the current month
 conn.execute("CREATE TABLE IF NOT EXISTS '%s' (ID INTEGER PRIMARY KEY, DAY INTEGER NOT NULL, AMOUNT FLOAT NOT NULL, TAG TEXT NOT NULL)" % _month)
 
 # insert record into the table
 conn.execute("INSERT INTO '%s' (DAY, AMOUNT,TAG) VALUES ('%d', '%f', '%s')" % (_month, int(_day), _amount, _tag))
 
 # save the transaction
 conn.commit()

 #display records 
 cursor = conn.execute("SELECT * FROM '%s'" %_month)
  
 for row in cursor:
  print "id:{}, date:{}, amount:{}, tag:{}".format(row[0], row[1], row[2], row[3])

 # close the database connection
 conn.close()






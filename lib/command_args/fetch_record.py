import sqlite3
import time
import datetime
import os
import sys
from progressive.bar import Bar



def process_request(obj):
 # check if year is mentioned
 if obj.year:
  _year = obj.year
 else:
  _year = datetime.datetime.now().strftime("%Y")
 
 if obj.month:
  _month = obj.month
 else:
  _month = datetime.datetime.now().strftime("%B")

 if obj.day:
  _day = obj.day
 else:
  _day = datetime.datetime.now().strftime("%d")

 # create a database connection
 path = os.path.join(os.path.dirname(__file__,), '..', '..', 'data', _year+'.db')
 conn = sqlite3.connect(path)

 # create object of Bar
 prog = Bar(filled_color=2, title=u'Fetching details , please wait ....')

 # create cursor object and clear lines
 prog.cursor.clear_lines(2)
 
 # save the state of the cursor
 prog.cursor.save()

 for i in range(101):
  time.sleep(0.02)
  prog.cursor.restore()
  prog.draw(i)

 #display records 
 cursor = conn.execute("SELECT * FROM '%s' WHERE DAY='%d'" %(_month, int(_day)))
 
 if cursor: 
  print "Successully fetched details"
 else:
  print "No details to fetch"
  sys.exit()
 # displaying results in nice tabular format [TODO]
 for row in cursor:
  print "id:{}, date:{}, amount:{}, tag:{}".format(row[0], row[1], row[2], row[3])


 # graphical representations [TODO]
 # close the database connection
 conn.close()





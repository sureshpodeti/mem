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

 _id = None 
 if obj.id:
  _id = obj.id

 # create a database connection
 path = os.path.join(os.path.dirname(__file__,), '..', '..', 'data', _year+'.db')
 conn = sqlite3.connect(path)

 # create object of Bar
 prog = Bar(filled_color=2, title=u'Deleting record , please wait ....')

 # create cursor object and clear lines
 prog.cursor.clear_lines(2)

 # save the state of the cursor
 prog.cursor.save()

 for i in range(101):
  time.sleep(0.02)
  prog.cursor.restore()
  prog.draw(i)
 

 # check if _id is present ,if yes delete that particular id record
 if _id:
  for _item in _id:
   cursor = conn.execute("DELETE FROM '%s' WHERE DAY='%d' AND ID='%d'" %(_month, int(_day), int(_item)))
 else:
 #display records 
  cursor = conn.execute("DELETE FROM '%s' WHERE DAY='%d'" %(_month, int(_day)))
 conn.commit()
 conn.close()

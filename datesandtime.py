import datetime
from datetime import date


#currentDate = datetime.date.today()
#print (currentDate.strftime("%d %b %y"))

d0 = datetime.date.today()
d1 = date(2004, 9, 21)
delta = d0 - d1
print (delta)
start_date = datetime.date.today() - delta

print(start_date.strftime('Please attend our event %A, %B %d in the year %Y'))

#print (start_date.strftime('Please attend event '%A %B %d in the Year %Y'))






import datetime
from datetime import date


d0 = datetime.date.today()
d1 = date(2027, 7, 20)
delta = d1 - d0
print (delta)
start_date = datetime.date.today() + delta

print(start_date.strftime('Please attend our event %A, %B %d in the year %Y'))


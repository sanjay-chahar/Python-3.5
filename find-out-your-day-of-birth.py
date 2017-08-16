import datetime
from datetime import date


#currentDate = datetime.date.today()
#print (currentDate.strftime("%d %b %y"))

# d0 = datetime.date.today()
# print(d0)
# year = int(input('Enter a year : '))
# month = int(input('Enter a month : '))
# day = int(input('Enter a day : '))
# d1 = datetime.date(year, month, day)
# print(d1)
# delta = d0 - d1
# print(delta)
# #print ('No of days remaining %d' % delta )
# start_date = datetime.date.today() + delta
#
# print(start_date.strftime('Please attend our event %A, %B %d in the year %Y'))



inPutdate = input('please enter your birthday (dd/mm/yyyy) : ')

birthday = datetime.datetime.strptime(inPutdate, '%d/%m/%Y').date()
days = birthday - datetime.date.today()
print(days)

import datetime

today = datetime.datetime.now().time()
today1 = datetime.date.today()
#print (today1)


x = datetime.datetime(year=2017, month=4, day=11)
print(x.year)
print(x.strftime("%c"))
print(x.strftime("%X"))
print(x.strftime("%x"))
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))


datetime_str = '09/19/18 13:55:26'
datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
print (datetime_object)

import pytz

print (pytz.all_timezones)

print ("India Time :", datetime.datetime.now())
aus_date = datetime.datetime.now(pytz.timezone('Australia/Sydney'))
mi_date = datetime.datetime.now(pytz.timezone('US/Michigan'))
print ("Aus Time", aus_date )
print ("MI Time", mi_date )



x = datetime.datetime(year=2017, month=4, day=11 , hour=10)
y = datetime.datetime(year=2018, month=4, day=11 , hour= 9)
delta= y-x
print (delta.days)
print (delta.seconds)

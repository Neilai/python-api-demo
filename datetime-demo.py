__author__ = "Neil"
__time__ = "2018/2/21 22:23"
import datetime
# a=datetime.date(2017, 3, 22)
a=datetime.date.today()
print(datetime.timedelta(days=1))
print(a)
print(a.year)
print(a.month)
print(a.day)
print(a.timetuple())
print(datetime.datetime.now())
__author__ = "Neil"
__time__ = "2018/2/21 22:13"
import time,datetime
import re

def processdatetime(x):
    today=datetime.date.today()
    year=today.year
    x = x.lstrip()
    x = x.rstrip()

    result = re.search(r"(\d+)秒前", x)
    if result:
        period = (datetime.datetime.now() - datetime.timedelta(seconds=int(result[1])))
        # 转换为时间戳:
        timeStamp = int(time.mktime(period.timetuple()))
        return timeStamp

    result=re.search(r"(\d+)分钟前",x)
    if result:
        period= (datetime.datetime.now() - datetime.timedelta(minutes=int(result[1])))
        #转换为时间戳:
        timeStamp = int(time.mktime(period.timetuple()))
        return timeStamp

    result=re.search(r"(\d+)小时前",x)
    if result:
        period= (datetime.datetime.now() - datetime.timedelta(hours=int(result[1])))
        #转换为时间戳:
        timeStamp = int(time.mktime(period.timetuple()))
        return timeStamp

    result=re.search(r"今天(.*)",x)
    if result:
        x=str(today)+result[1]
        timeStruct = time.strptime(str(x), "%Y-%m-%d %H:%M")
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp

    result=re.search(r"昨天(.*)",x)
    if result:
        x=str(today)+result[1]
        timeStruct = time.strptime(str(x), "%Y-%m-%d %H:%M")
        timeStamp = int(time.mktime(timeStruct))-24*60*60*1000
        return timeStamp


    result=re.search(r"(\d+)月(\d+)日 (\d+):(\d+)",x)
    if result:
        x=str(year)+"年"+x
        timeStruct = time.strptime(x, "%Y年%m月%d日 %H:%M")
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp

    result=re.search(r"(\d+)-(\d+)-(\d+) (\d+):(\d+)",x)
    if result:
        timeStruct = time.strptime(x,"%Y-%m-%d %H:%M")
        #转换为时间戳:
        timeStamp = int(time.mktime(timeStruct))
        return timeStamp






# 日期转换为时间戳
# t = "2017-11-24 17:30:00"
# #将其转换为时间数组
# timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
# print(timeStruct)
# #转换为时间戳:
# timeStamp = int(time.mktime(timeStruct))
# print(timeStamp)

# 时间戳转化为日期
# timeStamp = 1511515800
# localTime = time.localtime(timeStamp)
# strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
# print(strTime)

#格式切换
# t = "2017-11-24 17:30:00"
# #先转换为时间数组,然后转换为其他格式
# timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
# strTime = time.strftime("%Y/%m/%d %H:%M:%S", timeStruct)
# print(strTime)

# import datetime
# #先获得时间数组格式的日期
# threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
# #转换为时间戳:
# timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# #转换为其他字符串格式:
# strTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
# print(strTime)

print(processdatetime("1月23日 17:52"))
print(processdatetime("2017-11-29 21:07"))
print(processdatetime("今天 10:17"))
print(processdatetime("昨天 10:17"))
print(processdatetime("20分钟前"))
print(processdatetime("6小时前"))
print(processdatetime("6秒前"))
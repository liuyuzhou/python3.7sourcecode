#!/usr/bin/python
#-*- coding:UTF-8 -*-
import calendar
import datetime
import time

year = time.strftime("%Y", time.localtime())
mon  = time.strftime("%m", time.localtime())
day  = time.strftime("%d", time.localtime())
hour = time.strftime("%H", time.localtime())
min  = time.strftime("%M", time.localtime())
sec  = time.strftime("%S", time.localtime())

def today():
    '''''
    get today,date format="YYYY-MM-DD"
    '''''
    return datetime.date.today()

def todaystr():
    '''
    get date string, date format="YYYYMMDD"
    '''
    return year + mon + day

def date_time():
    '''''
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def datetimestr():
    '''''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year + mon + day + hour + min + sec


def get_day_of_day(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if n < 0:
        n = abs(n)
        return datetime.date.today() - datetime.timedelta(days=n)
    else:
        return datetime.date.today() + datetime.timedelta(days=n)

def get_days_of_month(year, mon):
    '''''
    get days of month
    '''
    return calendar.monthrange(year, mon)[1]

def get_firstday_of_month(year, mon):
    '''''
    get the first day of month
    date format = "YYYY-MM-DD"
    '''
    days = "01"
    if int(mon) < 10:
        mon = "0" + str(int(mon))
    arr = (year, mon, days)
    return "-".join("%s" %i for i in arr)

def get_lastday_of_month(year, mon):
    '''''
    get the last day of month
    date format = "YYYY-MM-DD"
    '''
    days=calendar.monthrange(year, mon)[1]
    mon = addzero(mon)
    arr = (year, mon, days)
    return "-".join("%s" %i for i in arr)

def get_firstday_month(n=0):
    '''''
    get the first day of month from today
    n is how many months
    '''
    (y, m, d) = getyearandmonth(n)
    d = "01"
    arr = (y, m, d)
    return "-".join("%s" %i for i in arr)


def get_lastday_month(n=0):
    '''''
    get the last day of month from today
    n is how many months
    '''
    return "-".join("%s" %i for i in getyearandmonth(n))

def getyearandmonth(n=0):
    '''''
    get the year,month,days from today
    befor or after n months
    '''
    thisyear = int(year)
    thismon = int(mon)
    totalmon = thismon + n
    if n >= 0:
        if totalmon <= 12:
            days = str(get_days_of_month(thisyear, totalmon))
            totalmon = addzero(totalmon)
            return year, totalmon, days
        else:
            i = totalmon//12
            j = totalmon%12
            if j == 0:
                i -= 1
                j = 12
            thisyear += i
            days = str(get_days_of_month(thisyear, j))
            j = addzero(j)
            return str(thisyear), str(j), days
    else:
        if totalmon > 0 and totalmon < 12:
            days = str(get_days_of_month(thisyear,totalmon))
            totalmon = addzero(totalmon)
            return year, totalmon, days
        else:
            i = totalmon//12
            j = totalmon%12
            if(j==0):
                i -= 1
                j = 12
            thisyear += i
            days = str(get_days_of_month(thisyear, j))
            j = addzero(j)
            return str(thisyear), str(j), days

def addzero(n):
    '''''
    add 0 before 0-9
    return 01-09
    '''
    nabs = abs(int(n))
    if nabs < 10:
        return "0" + str(nabs)
    else:
        return nabs

def get_today_month(n=0):
    '''''
    获取当前日期前后N月的日期
    if n>0, 获取当前日期前N月的日期
    if n<0, 获取当前日期后N月的日期
    date format = "YYYY-MM-DD"
    '''
    (y, m, d) = getyearandmonth(n)
    arr = (y, m, d)
    if int(day) < int(d):
        arr = (y, m, day)
    return "-".join("%s" %i for i in arr)

def get_firstday_month(n=0):
    (y, m, d) = getyearandmonth(n)
    arr = (y, m, '01')
    return "-".join("%s" %i for i in arr)

def main():
    print(f'today is:{today()}')
    print(f'today is:{todaystr()}')
    print(f'the date time is:{date_time()}')
    print(f'data time is:{datetimestr()}')
    print(f'2 days after today is:{get_day_of_day(2)}')
    print(f'2 days before today is:{get_day_of_day(-2)}')
    print(f'2 months after today is:{get_today_month(2)}')
    print(f'2 months before today is:{get_today_month(-2)}')
    print(f'2 months after this month is:{get_firstday_month(2)}')
    print(f'2 months before this month is:{get_firstday_month(-2)}')

if __name__=="__main__":
    main()

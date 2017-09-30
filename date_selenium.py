#!/usr/bin/env python
# coding=utf-8


import calendar
from datetime import date
import math


m = date.today()
currentYear, currentMonth, currentDay = m.year, m.month, m.day

weekdayof1st, totaldaysofmonth = calendar.monthrange(currentYear, currentMonth)
weekdayoflast = calendar.weekday(currentYear, currentMonth, totaldaysofmonth)

def getWeekNum():
    if (currentDay + weekdayof1st) < 6:
        weekofcurrday = 1
    else:
        weekofcurrday = math.ceil((currentDay + weekdayof1st - 6) / 7.0) + 1
    return weekofcurrday


import datetime

offset_month = 0
day_now = datetime.datetime.now().day
offset_year = 0

if 0 >= (datetime.datetime.now().day - 5):
    offset_month = -1
    day_now = 31 + (datetime.datetime.now().day - 5)

if 0 >= (datetime.datetime.now().month + offset_month):
    offset_year = -1
    offset_month = 11


date_now = datetime.datetime(year=(datetime.datetime.now().year + offset_year),
                             month=(datetime.datetime.now().month + offset_month),
                             day=day_now)

print(date_now)



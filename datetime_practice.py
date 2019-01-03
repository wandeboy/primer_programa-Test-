import datetime

user_date = 40

print('Do you want to know the date of how many days ago?')

while not user_date in range(0, 31):
    user_date = int(input('How many days?: '))
    if not user_date in range(0, 31):
        print('The days have to be between 1-31.')


offset_month = 0
day_now = datetime.datetime.now().day
offset_year = 0
day = datetime.datetime.now().day - user_date
month = datetime.datetime.now().month + offset_month

if 0 >= day:
    offset_month = -1
    day_now = 31 + day

month = datetime.datetime.now().month + offset_month
day = day_now

if 0 >= month:
    offset_year = -1
    offset_month = 11

month = datetime.datetime.now().month + offset_month

date_now = datetime.datetime(year=(datetime.datetime.now().year + offset_year),
                             month=month,
                             day=day)

print(date_now)

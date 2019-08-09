import datetime


now_time = datetime.datetime.now()
print('Ask me for a date')
day = int(input('Day[1-31]: '))
month = int(input('month[1-12]: '))
year = int(input('Year: '))
hour = input('And if you want the hour: ')
if hour == '':
    hour = 0
int(hour)
user_date = datetime.datetime(day=day, month=month, year=year, hour=hour)

date = user_date - now_time

print('{} hours'.format(date.total_seconds() / 60 / 60))



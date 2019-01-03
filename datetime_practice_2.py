import datetime

user_birthday_day = int(input('When is the day of your birthday? [1 - 31]: '))
user_birthday_month = int(input('When is the month of your birthday? [1 - 12] : '))
now_time = datetime.datetime.now()
user_year_bool = input('Your birthday already happened this year? [Y / N]: ').upper()

if user_year_bool == 'Y' or user_year_bool == 'YES':
    year = now_time.year + 1
else:
    year = now_time.year

user_birthday = datetime.datetime(year=year, month=user_birthday_month, day=user_birthday_day)
user_birthday_remaining = user_birthday - now_time
week_day_number = user_birthday.weekday()
month = user_birthday_remaining.days / 31
day = (user_birthday_remaining.days / 31 % 1) * 24
hour = user_birthday_remaining.seconds / 60 / 60
minute = ((user_birthday_remaining.seconds / 60 / 60) % 1) * 60
second = (minute % 1) * 60
week_day = ''

if week_day_number == 0:
    week_day = 'Monday'
elif week_day_number == 1:
    week_day = 'Tuesday'
elif week_day_number == 2:
    week_day = 'Wednesday'
elif week_day_number == 3:
    week_day = 'Thursday'
elif week_day_number == 4:
    week_day = 'Friday'
elif week_day_number == 5:
    week_day = 'Saturday'
elif week_day_number == 6:
    week_day = 'Sunday'

print('{} month, {} days, {} hours, {} minutes and {} seconds remaining'.format(int(month),
                                                                                int(day),
                                                                                int(hour),
                                                                                int(minute),
                                                                                int(second)))
print(week_day)



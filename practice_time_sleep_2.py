
from time import sleep
import datetime

NIGHT_STARTS = 21
DAY_STARTS = 6
HOUR_DURATION = 1


'''
        
'''


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_night = False
    alarm = ''
    weekday_day_dict = {'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3, 'viernes': 4, 'sabado': 5, 'domingo': 6}
    alarm_weekday = []
    count = 0

    while alarm != 's' and alarm != 'n':
        alarm = input('Deseas poner una alarma?[S/N]: ').lower()
    if alarm == 's':
        alarm_hour = int(input('A que hora quieres poner la alarma?[1-24]: '))
        weekday_time = int(input('Cuantos dias quieres que suene a la semana?: '))
        while count < weekday_time != 7:
            count += 1
            weekday = input('Que dias quieres que suene?: ')
            alarm_weekday.append(weekday)
    else:
        write_file_and_screen('No se configuro la alarma', 'horas.txt')
        alarm_weekday.append(None)

    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if alarm_weekday == [None]:
            pass

        elif not alarm_weekday:
            if current_time.hour == alarm_hour:
                write_file_and_screen("La alarma suena", 'horas.txt')
        elif alarm_weekday != [None]:
            for index in range(len(alarm_weekday)):
                if alarm_weekday[index] in weekday_day_dict:
                    if weekday_day_dict[alarm_weekday[index]] == current_time.weekday():
                        if current_time.hour == alarm_hour:
                            write_file_and_screen("La alarma suena", 'horas.txt')

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (DAY_STARTS < current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()


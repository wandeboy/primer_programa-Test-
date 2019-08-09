
from time import sleep
from random import randint


def main():
    string_list = []
    string_add = input('Write something ["END" for exit]: ')
    while string_add != 'END':
      string_list.append(string_add)
      string_add = input('Write something ["END" for exit]: ')

    while True:
        random_index = randint(0, len(string_list)-1)
        sleep(3)
        print(string_list[random_index])


if __name__ == '__main__':
    main()
    pass


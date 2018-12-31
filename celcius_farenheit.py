

f_or_c = "unknown"
temp = ""
print("\n")
print(" Conversion F/C ".center(50, "="))

while f_or_c != "f" and f_or_c != "c":
    f_or_c = input("IS Fahrenheit or Celsius? [F] / [C]: ").lower()

while not temp.isdigit():
    temp = input("what is your temperature?: ")
    if not temp.isdigit():
        print('do not put letters')

print('Temperature Add!')

if f_or_c == "f":
    conversion = (float(temp) - 32)/1.8
    print("Your temp is the same that {}ºC".format(conversion))
elif f_or_c == "c":
    conversion = float(temp) * 1.8 + 32
    print("Your temp is the same that {}ºF".format(conversion))



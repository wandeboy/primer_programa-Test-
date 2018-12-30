

f_or_c = "unknown"

print("\n")
print(" Conversion F/C ".center(50, "="))

while f_or_c != "f" and f_or_c != "c":
    f_or_c = input("IS Fahrenheit or Celsius? [F] / [C] ").lower()

temp = float(input("what is your temperature? (only number)"))

if f_or_c == "f":
    conversion = (temp - 32)/1.8
    print("{}ºC".format(conversion))
elif f_or_c == "c":
    conversion = temp * 1.8 + 32
    print("{}ºF".format(conversion))



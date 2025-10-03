FAHRENHEIT_TO_CELSIUS = 0
CELSIUS_TO_FAHRENHEIT = 0
def convert_to_celsius(FAHRENHEIT_TO_CELSIUS):
    FAHRENHEIT_TO_CELSIUS_FACTOR = (FAHRENHEIT_TO_CELSIUS - 32) * 5/9
    print(FAHRENHEIT_TO_CELSIUS_FACTOR)
def convert_to_fahreneit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = (CELSIUS_TO_FAHRENHEIT * 9/5) + 32
    print (CELSIUS_TO_FAHRENHEIT_FACTOR)
c_or_f = int(input("Enter the temperature to convert: "))
check = input("Is this temperature in Celsius or Fahrenheit?(C/F): ")
if check == "f":
    convert_to_celsius(c_or_f)
elif check == "c":
    convert_to_fahreneit(c_or_f)
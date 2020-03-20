# temperataure converter

# units of temperature
print("""
Units of temperature are : 

1. celsius
2. fahrenheit
3. kelvin
4. rankine
5. delisle
6. newton""")

# use converter

a = input("To use converter press 'c' OR to close the program press any key   key = ")

# convert

if a == 'c':
    actual_unit = input("enter the present unit : ")
    convert_unit = input("enter the unit in which you have to convert : ")
    number1 = float(input("Enter the actual no : "))
    if actual_unit == 'celsius':
        if convert_unit == 'celsius':
            print(number1)
        elif convert_unit == 'fahrenheit':
            print(number1 * (9 / 5) + 32)
        elif convert_unit == 'kelvin':
            print(number1 + 273.15)
        elif convert_unit == 'rankine':
            print((number1 + 273.15) * (9 / 5))
        elif convert_unit == 'delisle':
            print((100 - number1) * (3 / 2))
        elif convert_unit == 'newton':
            print(number1 * (33 / 100))

    if actual_unit == 'Fahrenheit':
        if convert_unit == 'celsius':
            print((number1 - 32) * (5 / 9))
        elif convert_unit == 'fahrenheit':
            print(number1)
        elif convert_unit == 'kelvin':
            print((number1 + 459.67) * (5 / 9))
        elif convert_unit == 'rankine':
            print(number1 + 459.67)
        elif convert_unit == 'delisle':
            print((212 - number1) * (5 / 6))
        elif convert_unit == 'newton':
            print((number1 - 32) * (11 / 60))

    if actual_unit == 'kelvin':
        if convert_unit == 'celsius':
            print(number1 - 273.15)
        elif convert_unit == 'fahrenheit':
            print((number1 * (9 / 5)) - 459.67)
        elif convert_unit == 'kelvin':
            print(number1)
        elif convert_unit == 'rankine':
            print(number1 * (9 / 5))
        elif convert_unit == 'delisle':
            print(373.15 - number1 * (3 / 2))
        elif convert_unit == 'newton':
            print((number1 - 273.15) * (33 / 100))

    if actual_unit == 'newton':
        if convert_unit == 'celsius':
            print(number1 * (100 / 33))
        elif convert_unit == 'fahrenheit':
            print(number1 * (60 / 11) + 32)
        elif convert_unit == 'kelvin':
            print(number1 * (100 / 33) + 273.15)
        elif convert_unit == 'rankine':
            print(number1 * (60 / 11) + 491.67)
        elif convert_unit == 'delisle':
            print(33 - number1 * (50 / 11))
        elif convert_unit == 'newton':
            print(number1)

    if actual_unit == 'rankine':
        if convert_unit == 'celsius':
            print(number1 - 491.67 * (100 / 33))
        elif convert_unit == 'fahrenheit':
            print(number1 - 459.67)
        elif convert_unit == 'kelvin':
            print(number1 * (5 / 9))
        elif convert_unit == 'rankine':
            print(number1)
        elif convert_unit == 'delisle':
            print(671.67 - number1 * (5 / 6))
        elif convert_unit == 'newton':
            print((number1 - 491.67) * (11 / 60))

    if actual_unit == 'delicle':
        if convert_unit == 'celsius':
            print(100 - number1 * (2 / 3))
        elif convert_unit == 'fahrenheit':
            print(212 - number1 * (6 / 5))
        elif convert_unit == 'kelvin':
            print(373.15 - number1 * (2 / 3))
        elif convert_unit == 'rankine':
            print(671.67 - number1 * (6 / 5))
        elif convert_unit == 'delisle':
            print(number1)
        elif convert_unit == 'newton':
            print(33 - number1 * (11 / 50))

#    else:
#       print("wrong input")
#       exit()
                                                                                                                                                       
# exit the program

else:
    exit()

#Welcome the user
print("""WELCOME IN THE TEMPERATURE CONVERTER PROGRAM
-----------------------------------------------
This program will convert the temperature from Fahrenheit to Celcius and vice versa.""")

#intialize the variable choice with empty string
choice = ""

#based on his choice condition 1 or 2 will be execute. Set the condition to be equal to 1 or 2 otherwise the user should introduce again a number
while choice != 1 and choice != 2:
    choice = int(input("Introduce 1 for Fahrenheit to Celcius or 2 for Celcius to Fahrenheit -> "))#put in a variable the user's choice
    if choice == 1:
        fahrenheit_temp = (float(input("Enter a temperature in Fahrenheit: ")))
        celcius_temp = (fahrenheit_temp - 32) * 5/9 #celcius formula
        print("The temperature in Celcius is", round(celcius_temp, 2))
    elif choice == 2:
        celcius_temp = float(input("Enter a temperature in Celcius: "))
        fahrenheit_temp = (celcius_temp * 9/5) + 32 #fahrenheit formula
        print("The temperature in Fahrenheit is", round(fahrenheit_temp))
    else:
        print("Please make a choice between number 1 or 2") #if the user introduce a number different than 1 or 2, the program will ask him to introduce again a number

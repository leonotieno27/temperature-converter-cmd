"""Program to convert fahrenheit to celsius and celsius to fahrenheit"""

import os

def main():
    print('\t\t\t*** Temperature Converter ***\t\t\t')

    print("choose Convert option(use numbers):")
    print("1. Celsius To Fahrenheit")
    print("2. Fahrenheit To Celsius")
    choice = input()

    #if required input call the function
    if int(choice) == 1:
        celsiusToFahrenheit()
    elif int(choice) == 2:
        fahrenheitToCelsius()
    else:
        print("Input out of range!")
        choice2 = input("Do you want to try again?(Y/N)")
        if choice2.upper() == 'Y':
            os.system('clear')
            main()
        elif choice2.upper() == 'N':
            quit()  #close program


#convert celsius to fahrenheit
def celsiusToFahrenheit():
    os.system('clear')
    print('\t\t\t*** Temperature Converter ***\t\t\t')
    celsius = float(input("Enter the value in °C: ")) #change data type to float
    ans = (celsius * (9/5)) + 32
    print(f"{celsius}°C is Equal to {ans}F")
 
 # convert fahrenheit to celsius
def fahrenheitToCelsius():
    os.system('clear')  #clear terminal screen
    print('\t\t\t*** Temperature Converter ***\t\t\t')
    fahr = float(input("Enter the value in Fahrenheit: ")) #type-casting to user input to float
    ans = 5/9 * (fahr - 32) 
    print(f"{fahr}F is equal to {ans}°C")

main()
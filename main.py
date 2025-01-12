"""Program to convert fahrenheit to celsius and celsius to fahrenheit"""

import os

def main():
    print('\t\t\t*** Temperature Converter ***\t\t\t')

    print("Convert:")
    print("1. Celsius To Fahrenheit")
    print("2. Fahrenheit To Celsius")
    choice = input()

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
            quit()


def celsiusToFahrenheit():
    os.system('clear')
    print('\t\t\t*** Temperature Converter ***\t\t\t')
    celsius = float(input("Enter the value in °C: "))
    ans = (celsius * (9/5)) + 32
    print(f"{celsius}°C is Equal to {ans}F")
 
def fahrenheitToCelsius():
    os.system('clear')
    print('\t\t\t*** Temperature Converter ***\t\t\t')
    fahr = float(input("Enter the value in Fahrenheit: "))
    ans = 5/9 * (fahr - 32) 
    print(f"{fahr}F is equal to {ans}°C")

main()
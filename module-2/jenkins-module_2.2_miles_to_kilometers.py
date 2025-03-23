"""
Author: Jelani Jenkins
Date: 01/25/2025

Write a program that uses a function to convert miles to kilometers.
Your program should prompt the user for the number of miles driven then
call a function which converts miles to kilometers. 
Check and validate all user input and incorporate Try/Except block(s). 
The program should then display the total miles and the kilometers.

"""
import traceback

def main():
    while True:
        try:
            miles = float(input("Miles driven: "))# Prompt user
            if miles < 0:
                raise ValueError("Miles cannot be negative. Please enter a positive number.")
            # Lambda expresion to convert to kilometers
            kilometers = (lambda miles: miles * 1.60934)(miles)
            print(f"\nTotal miles: {miles:.2f}")
            print(f"Kilometers: {kilometers:.2f}")
            break

        except ValueError as e:
            print(f"Invalid input: {e}.\n")
        except Exception as ex:
            print(f"An error occurred: {ex}")
            print(f"Traceback error: {traceback.format_exc()}")

if __name__ == "__main__":
    main()

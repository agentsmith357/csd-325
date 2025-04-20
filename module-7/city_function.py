'''

Author: Jelani Jenkins
Date: 10/12/2023
Course: Advanced Python Programming 325
Assignment: City Functions

Write a function that accepts two parameters: a city name and a country name. 
The function should return a single string of the form City, Country, such as Santiago, Chile.
Store the function in a file named city_functions.py. 

In the same file, call the function at least three times using a City, Country values. 
Excecute city_functions.py and take a screenshot of the result. Paste that screenshot into your Word document.

'''

def city_country(city, country,language=None,population=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f" - language {language}"
    return result


'''
Author: Jelani Jenkins
Date: 04/27/2025
Course: Advanced Python Programming 325
Module:JSON and Application Programming Interfaces

Create a Python program to use for the tutorial. Use the correct URL listed above in the Reading List to test the connection, run the program, take a screenshot of the results and paste into the Word document. 
Complete the section in the tutorial for retrieving current astronauts and formatting output. Incorporate that code into your program, run the program and take a screenshot of the results and paste into the Word document.
Create a program that includes the following:
Find a simple API. The link above has a couple that you can work with, but the examples are not in Python...the concept is the same..
Test the connection to your API, output results.
Print out the response from the request, with no formatting.
Print out the response with same formatting as the tutorial program.
Run the program and take a screenshot of the results. Paste that screenshot into your Word document.
'''

from pathlib import Path
import requests
import os, sys
from dotenv import dotenv_values
BASE_DIR = Path(__file__).resolve().parent.parent # get the current working directory
#using our .env file
ENV = Path(os.path.join(BASE_DIR,".env"))
if os.path.exists(ENV):
    secrets = dotenv_values(ENV) # load the .env file
else:
    sys.exit("No .env file found.")

URL = "http://api.open-notify.org/astros.json"
response = requests.get(URL)
print(f"Response Code: {response.status_code}")
if response.status_code == 200:
    peoples = response.json()['people']
    print(f"Number of people: {response.json()['number']}")
    print("People in space:")
    for people in peoples:
        print(f"{people['name']} is on the {people['craft']}")
    print("")

URL2 = f"https://api.nasa.gov/planetary/apod?api_key={secrets['API_KEY']}"
response = requests.get(URL2)
print(f"Response Code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Explanation: {data['explanation']}")
    print(f"URL: {data['url']}")
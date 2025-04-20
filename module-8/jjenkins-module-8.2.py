
'''
Author: Jelani Jenkins
Date: 10/12/2023
Course: Advanced Python Programming 325
Assignment: JSON practice
'''

# load parameters
import json, os
from pathlib import Path
BASE_DIR = Path.cwd()
JSON_FILE = os.path.join(BASE_DIR,"module-8","student.json")
student_list =[]

# Use the JSON load()  function to load the file into a Python class list.
with open(JSON_FILE, "r") as file:
    student_list = json.load(file)

def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

print("Original Student List:")
print_students(student_list)

#Add your last name, first name, fictional ID, and email to the class list using append().

new_student = {
    "F_Name": "Jelani",
    "L_Name": "Jenkins",
    "Student_ID": 123456,
    "Email": "jeljenkins@my365.bellevue.edu"
}
student_list.append(new_student)


print("\nUpdated Student List:")
print_students(student_list)

with open(JSON_FILE, "w") as file:
    json.dump(student_list, file)

print("\nThe student.json file was updated.")
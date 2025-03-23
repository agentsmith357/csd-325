"""
Jelani Jenkins
Module 1.3
Date: 03/23/2025

Assignment: On the Wall + Flowchart(s)
For this assignment, you have two tasks. The first is to create a flowchart (or flowcharts) for the following requirements, then to write a Python program that produces the required results:
If you are not familiar with the reverse counting song "100 bottles of beer on the wall", you'll need to do a little research to familiarize yourself with it.
Ask the user how many bottles of beer are on the wall.
Pass that input to a function that manages the countdown.
The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
Once the count is down to 1, change lyrics to show "1 bottle of beer..."
At the end of the countdown, get back to the main program and remind the user to buy more beer.
The output should look similar to:

Open up a drawing application. Use a text element to include your name and assignment number at the top of the drawing. Before continuing, you might view the Flowchart and Structures video listed in the Module Reading area. Then, create a flowchart that models the above process.  Copy/paste the diagram into a Word document and save to your module-1 directory.
Create a Python program that addresses the requirements of the process above. Save the file to your module-1 directory.

"""

try:
    X = int(input("Enter number of bottles:"))
    Y = X
    while X > 1:
        X = Y
        Y = X - 1
        if X == 1:
            print(f"{X} bottle of beer on the wall, {X} bottle of beer.")
            print(f"Take one down and pass it around, {Y} bottle(s) of beer on the wall.\n")
        else:
            print(f"{X} bottles of beer on the wall, {X} bottles of beer.")
            print(f"Take one down and pass it around, {Y} bottle(s) of beer on the wall.\n")

    print("Time to buy more bottles of beer.")
except Exception as e:
    print("An error occurred:", e)

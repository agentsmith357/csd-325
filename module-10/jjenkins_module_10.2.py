"""
Author: Jelani Jenkins
Date: 05/01/2025
Assignment: Module 10.2 Updating Tinker App

Read through the end of Section 2 in the tutorial and copy the code in Listing 2.2 Our Scrolling To-Do. Paste into your Python program and save to your module-10 directory. Run the program, add a couple of tasks, and take a screenshot of the output and paste into the Word document.
Using the other items in the reading list, complete the following modifications:
Change the Title of the window to your last name-ToDo. Ex. Sampson-ToDo
Change the color of the menu items, two (2) complementary colors work best.
Currently, the user clicks the left mouse button to delete a task.. change that to the right mouse button.
Provide instructions in the label on how to delete a task.
We want the user to exit correctly, so add a menu item of File -> Exit. When clicked, Exit will end the program.
Run the program, add a few tasks and take a screenshot. Paste that screenshot into your Word document.
As the program is running, delete a task, then take a screenshot. Paste that screenshot into your Word document.

"""
import tkinter as tk
from tkinter import Menu

def delete_task(event):
    event.widget.destroy()

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def add_task(event=None):
    task = entry.get()
    if task:
        task_label = tk.Label(task_frame, text=task, bg="gold", fg="black", pady=5)
        task_label.pack(fill='x', padx=5, pady=2)

        task_label.bind("<Button-3>", delete_task)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Jenkins-ToDo")  # Change window title

menu_bar = Menu(root, bg="purple", fg="white")
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, bg="purple", fg="white")
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.destroy)

instruction = tk.Label(root, text="Item Added --- Right Click Item to Delete ", bg="plum", fg="black")
instruction.pack(fill='x')

entry = tk.Entry(root, font=('Arial', 14))
entry.pack(padx=10, pady=10, fill='x')
entry.bind("<Return>", add_task)

task_frame = tk.Frame(root, bg="lightgray")
task_frame.pack(expand=True, fill='both')

canvas = tk.Canvas(task_frame, bg="lightgray")
scroll_y = tk.Scrollbar(task_frame, orient="vertical", command=canvas.yview)
task_container = tk.Frame(canvas, bg="lightgray")

task_container.bind("<Configure>", update_scroll_region)

canvas.create_window((0, 0), window=task_container, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

task_frame = task_container
root.mainloop()
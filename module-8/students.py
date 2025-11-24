# Christopher Villarreal
# Module 9 - Assignment 2
# November 23, 2025
# Purpose: This program reads a JSON file containing student information,
#          adds a new student's information to the list, updates the JSON file,
#          and notifies the user with a message box.

import json
import tkinter as tk
from tkinter import messagebox

# Main Function
def main():
    file_name = 'student.json'
    # Load student.json file
    with open(file_name) as f:
        students = json.load(f)

    print("Provided is the Original Student List: \n")
    print_student_info(students)
    print("")

    # Add new student information (me)
    new_student = {
        "F_Name": "Christopher",
        "L_Name": "Villarreal",
        "Student_ID": 241876,
        "Email": "cvillarreal@gmail.com"
    }

    # Add's the new student to the python list (Not the json file)
    students.append(new_student)

    print("Student list has been updated! \n")
    print_student_info(students)
    print("")

    # Save the updated list back to student.json
    with open(file_name, 'w') as f:
        json.dump(students, f, indent=4)

    # Prompt user with a message box indicating the file has been updated
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("File Modified", f"The file {file_name} has been updated!")

    print(f"{file_name} has been updated with the new student information.")

# Function will loop through the student list and print each student's information
def print_student_info(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

if __name__ == "__main__":
    main()

# References
# Idea from user (Dan) on discord
# https://docs.python.org/3/library/tkinter.messagebox.html#module-tkinter.messagebox
# https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window

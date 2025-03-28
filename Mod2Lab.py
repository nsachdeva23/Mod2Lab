# Name: Nandini Sachdeva
# File name: Mod2Lab.py
# This app will prompt the user to input their name and GPA and will then determine and display if the student has made the honor roll or dean's list.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
while last_name != "ZZZ":
    gpa = float(input("What is your gpa? "))
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List and the Honor Roll.")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll.")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    



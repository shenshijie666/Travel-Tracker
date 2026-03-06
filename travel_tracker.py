"""
CP1404 Assignment 1 - Travel Tracker
Author: shenshijie666
"""

MENU = """Menu:
D - Display all places
R - Recommend a random place
A - Add a new place
M - Mark a place as visited
Q - Quit
"""

print("Travel Tracker 1.0 - by shenshijie666")

choice = ""
while choice != "Q":
    print(MENU)
    choice = input(">>> ").upper()

    if choice == "D":
        print("Display all places")
    elif choice == "R":
        print("Recommend a random place")
    elif choice == "A":
        print("Add a new place")
    elif choice == "M":
        print("Mark a place as visited")
    elif choice == "Q":
        print("Have a nice day :)")
    else:
        print("Invalid menu choice")

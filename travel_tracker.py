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
import random

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

# load places from csv
places = []

with open("places.csv") as file:
    for line in file:
        parts = line.strip().split(",")
        parts[2] = int(parts[2])      # convert priority
        places.append(parts)

print(f"{len(places)} places loaded from places.csv")

# display places list
def display_places_basic():
    for place in places:
        print(place)

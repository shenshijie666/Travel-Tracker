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

# improved displayed places formatting
def display_places():
    count = 0
    for place in places:
        count += 1
        name = place[0]
        country = place[1]
        priority = place[2]
        visited = place[3]

        marker = "* " if visited == "n" else "  "

        print(f"{marker}{count}. {name:10} in {country:15} priority {priority}")

# unvisited places counter
def count_unvisited():
    count = 0
    for place in places:
        if place[3] == "n":
            count += 1
    return count


def show_summary():
    total = len(places)
    unvisited = count_unvisited()
    print(f"{total} places tracked. You still want to visit {unvisited} places.")

# recommend random unvisited place

def recommend_place():
    unvisited = [place for place in places if place[3] == "n"]

    if not unvisited:
        print("No places left to visit!")
    else:
        place = random.choice(unvisited)
        print(f"Why not visit {place[0]} in {place[1]}?")

# create a new place entry
def add_place():
    name = input("Name: ")
    country = input("Country: ")
    priority = int(input("Priority: "))

    places.append([name, country, priority, "n"])
    print(f"{name} in {country} (priority {priority}) added.")



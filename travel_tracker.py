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
    display_menu()
    choice = input(">>> ").upper()

    if choice == "D":
        display_places()
        show_summary()

    elif choice == "R":
        recommend_place()

    elif choice == "A":
        add_place()

    elif choice == "M":
        mark_visited()

    elif choice == "Q":
        save_places()
        print("Goodbye!")

    else:
        print("Invalid option")

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
    while name == "":
        print("Input cannot be blank")
        name = input("Name: ")

    country = input("Country: ")
    while country == "":
        print("Input cannot be blank")
        country = input("Country: ")

    valid = False
    while not valid:
        try:
            priority = int(input("Priority: "))
            if priority > 0:
                valid = True
            else:
                print("Priority must be > 0")
        except ValueError:
            print("Invalid input")

    places.append([name, country, priority, "n"])
    print(f"{name} in {country} (priority {priority}) added.")

# mark as visited

def mark_visited():
    display_places()

    try:
        choice = int(input("Enter place number: "))

        if choice <= 0:
            print("Number must be > 0")
            return

        index = choice - 1

        if index >= len(places):
            print("Invalid place number")
            return

        if places[index][3] == "v":
            print("You have already visited this place")
        else:
            places[index][3] = "v"
            print(f"{places[index][0]} in {places[index][1]} visited!")

    except ValueError:
        print("Invalid input")

# save places to CSV when quitting
def save_places():
    with open("places.csv", "w") as file:
        for place in places:
            line = ",".join([place[0], place[1], str(place[2]), place[3]])
            file.write(line + "\n")

    print(f"{len(places)} places saved to places.csv")






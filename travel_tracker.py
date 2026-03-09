"""
CP1404 Assignment 1 - Travel Tracker
Author: Shen Shijie
JCU ID: 14568553
"""

import random

MENU = """Menu:
D - Display all places
R - Recommend a random place
A - Add a new place
M - Mark a place as visited
Q - Quit
"""

print("Travel Tracker 1.0 - by Shen Shijie")

# load places
places = []
with open("places.csv") as file:
    for line in file:
        parts = line.strip().split(",")
        parts[2] = int(parts[2])
        places.append(parts)

print(f"{len(places)} places loaded from places.csv")


def display_menu():
    """Display menu options"""
    print(MENU)


def display_places():
    """Display all places sorted by visited then priority"""
    places.sort(key=lambda p: (p[3], p[2]))

    count = 0
    for place in places:
        count += 1
        name = place[0]
        country = place[1]
        priority = place[2]
        visited = place[3]

        marker = "*" if visited == "n" else " "

        print(f"{marker}{count}. {name:10} in {country:15} {priority}")


def count_unvisited():
    """Count unvisited places"""
    count = 0
    for place in places:
        if place[3] == "n":
            count += 1
    return count


def show_summary():
    """Display summary"""
    total = len(places)
    unvisited = count_unvisited()
    print(f"{total} places tracked. You still want to visit {unvisited} places.")


def recommend_place():
    """Recommend random unvisited place"""
    unvisited = [place for place in places if place[3] == "n"]

    if not unvisited:
        print("No places left to visit!")
    else:
        place = random.choice(unvisited)
        print("Not sure where to visit next?")
        print(f"How about... {place[0]} in {place[1]}?")


def add_place():
    """Add new place"""
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
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")

    places.append([name, country, priority, "n"])

    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_visited():
    """Mark place as visited"""

    if count_unvisited() == 0:
        print("No unvisited places")
        return

    display_places()

    try:
        choice = int(input("Enter the number of a place to mark as visited\n>>> "))

        if choice <= 0:
            print("Number must be > 0")
            return

        index = choice - 1

        if index >= len(places):
            print("Invalid place number")
            return

        if places[index][3] == "v":
            print(f"You have already visited {places[index][0]}")
        else:
            places[index][3] = "v"
            print(f"{places[index][0]} in {places[index][1]} visited!")

    except ValueError:
        print("Invalid input; enter a valid number")


def save_places():
    """Save places to CSV"""
    with open("places.csv", "w") as file:
        for place in places:
            line = ",".join([place[0], place[1], str(place[2]), place[3]])
            file.write(line + "\n")

    print(f"{len(places)} places saved to places.csv")


# main program loop
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
        print("Have a nice day :)")

    else:
        print("Invalid menu choice")
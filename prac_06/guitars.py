"""
Estimated Time: 20 Minutes
Actual Time: 37 minutes
"""

from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print("")
    name = input("Name: ")

print("")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>12} ({guitar.year}), worth ${guitar.cost:6,.2f}{vintage_string}")
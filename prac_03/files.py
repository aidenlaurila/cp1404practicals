"""
CP1404 - Practical
Files program
"""

# 1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())

print(number_1 + number_2)

# 4.
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number

print(total)
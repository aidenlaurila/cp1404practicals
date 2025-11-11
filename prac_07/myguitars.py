from guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """..."""
    guitars = convert_file_to_guitars(FILENAME)
    guitars.sort()
    add_guitar(guitars)
    [print(guitar) for guitar in guitars] # Debugging

def convert_file_to_guitars(filename):
    """..."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars

def add_guitar(guitars):
    """Adds guitar to list of guitars until user input is empty."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        print("")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


main()
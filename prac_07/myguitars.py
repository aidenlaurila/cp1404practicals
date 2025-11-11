from guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """Program to enable user to add guitars to a file of guitars."""
    guitars = load_guitars_from_file(FILENAME)
    add_guitar(guitars)
    guitars.sort()
    save_guitars_to_file(FILENAME, guitars)

def load_guitars_from_file(filename):
    """Loads all guitars from a file into guitars list."""
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
    """Appends guitar to list of guitars until entered input is empty."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        print("")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

def save_guitars_to_file(filename, guitars):
    """Write all guitars in list to file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
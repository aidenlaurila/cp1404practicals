from guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """..."""
    guitars = convert_file_to_guitars(FILENAME)
    guitars.sort()
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

main()
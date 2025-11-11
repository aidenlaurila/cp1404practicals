from guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """"""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        print(guitar) # Debugging
        guitars.append(guitar)
    in_file.close()

main()
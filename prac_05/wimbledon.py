"""
Emails
Estimate: 25 minutes
Actual: 32 minutes (I took a break)
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Loads and processes records to show statistics from wimbledon games"""
    records = load_records(FILENAME)
    champions_to_wins, winning_countries = process_records(records)
    print_results(champions_to_wins, winning_countries)

def load_records(filename):
    """Loads game records from CSV file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            section = line.strip().split(",")
            records.append(section)

    return records

def process_records(records):
    """Processes records into dictionary"""
    winning_countries = set()
    champion_to_wins = {}

    for record in records:
        winning_countries.add(record[COUNTRY_INDEX])

        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1

        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1

    return champion_to_wins, winning_countries

def print_results(champion_to_wins, winning_countries):
    """Prints champion and country results from processed records"""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)

    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))

main()
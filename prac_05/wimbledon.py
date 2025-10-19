"""
Emails
Estimate: 25 minutes
Actual:
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    records = load_records(FILENAME)
    champions_to_wins, winning_countries = process_records(records)
    print(champions_to_wins)
    print(winning_countries)

def load_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            section = line.strip().split(",")
            records.append(section)

    return records

def process_records(records):
    winning_countries = set()
    champion_to_wins = {}

    for record in records:
        winning_countries.add(record[COUNTRY_INDEX])

        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1

        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1

    return champion_to_wins, winning_countries

main()
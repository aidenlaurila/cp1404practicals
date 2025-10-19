"""
Emails
Estimate: 25 minutes
Actual:
"""
FILENAME = "wimbledon.csv"

def load_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            section = line.strip().split(",")
            records.append(section)
    return records

records2 = load_records(FILENAME)
print(records2)
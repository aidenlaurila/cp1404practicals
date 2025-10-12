"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_subject_data(FILENAME)
    print_subject_details(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject_data.append(parts)
    input_file.close()
    return subject_data

def print_subject_details(subject_data):
    """Print subject details."""
    max_name_length = max(len(subject[1]) for subject in subject_data)
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]:{max_name_length}} and has {subject[2]:3} students")

main()
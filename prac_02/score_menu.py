"""Complete program to process user score based on options"""

MENU = """(G)et a valid score
(P)rint results
(S)how stars
(Q)uit)"""

def main():
    """Get user score and process score based on options"""
    score = get_valid_score()
    print(MENU)
    choice = input('>>> ').upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = calculate_result(score)
            print(result)
        elif choice == "S":
            print_stars(int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input('>>> ').upper()
    print('goodnight')


def get_valid_score():
    """Prompt user until valid score is entered"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = float(input("Enter score: "))
    return score

def calculate_result(score):
    """Calculate result based on score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print as many stars as the score"""
    print('*' * score)

main()
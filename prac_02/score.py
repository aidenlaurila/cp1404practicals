"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    """Display user grade and random grade based on score"""
    score = float(input("Enter score: "))
    grade = calculate_result(score)
    print(f"Your grade is {grade}")

    random_score = random.randint(0, 100)
    grade = calculate_result(random_score)
    print(f"Random score of {random_score} is {grade}")

def calculate_result(score):
    """Calculate result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

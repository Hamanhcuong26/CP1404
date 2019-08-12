"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def score_status(score):
    if score < 0:
        status = "Invalid score"
    else:
        if score > 100:
            status = "Invalid score"
        if score > 50:
            status = "Passable"
        if score > 90:
            status = "Excellent"
    if score < 50:
        status = "Bad"
    return status


def main():
    score = float(input("Enter score: "))
    print(score_status(score))

    
main()


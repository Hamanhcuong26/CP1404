"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter integer Number"))
        finished = True
        result = number
    except  NameError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
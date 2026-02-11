import random

def NumberGuess():
    randomnumber=random.randint(1, 10)
    while randomnumber != inputs:
        inputs=int(input("Guess the Number:"))
    if randomnumber != inputs:
        print("Wrong")
    return
elif randomnumber == inputs:

    
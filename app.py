import random

randomnumber=random.randint(1,10)
def NumberGuess():
      History=[] 
      while True:
        Guess=int(input("What is the number?"))
        History.append(Guess)
        if Guess == randomnumber:
             print (f"Correct, you guessed {randomnumber}!")
             print("Your Guesses were:")
             for i in History:
                  print(i)
             break
        elif Guess > randomnumber:
             print ("Lower")
        else :
             print ("Higher")
             

NumberGuess()

     
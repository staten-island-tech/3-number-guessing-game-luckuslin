import random

randomnumber=random.randint(1, 10)
def NumberGuess():
      while True:
        Guess=int(input("What is the number?"))
        if Guess == range(1,10):
              return Guess
        else : 
            print ("Wrong Range")

def Check(randomnumber,Guess):
        if Guess == randomnumber:
             return "Correct"
        elif Guess > randomnumber:
             return "Too High"
        else :
             return "Too Low"

def History():
     Guesshistory=Check
     Guesshistory=0
     while Guesshistory < 10:
        Guesshistory + 1
     
History ()
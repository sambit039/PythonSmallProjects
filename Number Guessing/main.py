import random
from Art import art

EASY_LEVEL=10
HARD_LEVEL=5

turns=0
def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low.")
        return turns-1
    else:
        print(f"you got it.The answer was {answer}")

        
def set_difficulty():
    level=input("CHOSE DIFFICULTY,easy or hard-").lower()
    if level=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
 
   
def game():
    print(art)
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    answer=random.randint(1,100)
    print(f"The correct answer is {answer}")


    turns=set_difficulty()
    
    guess=0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("make a guess-")) 

        turns=check_answer(guess, answer,turns)
        if turns==0:
            print("You lose")
            return
        
game()


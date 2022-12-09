import random
from data import data
from art import logo,vs
from replit import clear

score=0


def format_data(account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    print(f"{account_name} a {account_description} from {account_country}")

def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="A"
    else:
        return guess=="B"
    
    

print(logo)
game_over=False

account_b=random.choice(data)

while not game_over:
    account_a=account_b
    
    while account_a==account_b:
        account_b=random.choice(data)
        
    format_data(account_a)
    print("vs")
    format_data(account_b)

    guess=input("Who has more followers?, 'A' or 'B'").upper()

    a_followers=account_a["follower_count"]
    b_followers=account_b["follower_count"]

    is_correct=check_answer(guess,a_followers,b_followers)
    
    clear()
    if is_correct:
        score+=1
        print(f"You are right, Current score: {score}")
        
    else:
        print(f"Sorry, Thats Wrong.Final score: {score}")
        game_over=True
        

    
    

        




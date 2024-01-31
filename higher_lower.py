from higher_lower_data import data
import random
import sys
import os 

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

''' THIS IS ONE ENTRY IN THE DATA LIST, EVERY MEMBER OF THE LIST IS A DICTIONARY WITH KEYS NAME, FOLLOWER_COUNT, DESCRIPTION AND COUNTRY
{
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },'''
correct_guess = 0
def higher_lower():
    
    print("You are playing HIGHER/LOWER. Please wait while we load the data.")
    account_A = random.choice(data)
    account_B = comparison_data(account_A)
    play(account_A, account_B)



def comparison_data(account_A):
    compare_with = random.choice(data)
    
    if compare_with == account_A:
        comparison_data()
    else:
        
        return compare_with
    
def next_guess(account_B):
    
    
    pass
def new_game():
    ng = input("Do you want to play new game(Y/N)\n")
    if ng.lower() == "y":
        os.system("cls")
        higher_lower()
    else:
        print("You chose to exit the game\nBYE")
        sys.exit()

def play(account_A, account_B):
    global correct_guess
    followers_a = account_A["follower_count"]
    followers_b = account_B["follower_count"]
    #You always compare account B to account A and then if you guess correctly acc B becomes acc A and B needs another random input from data. Else you lose
    b_is_bigger = True if followers_b > followers_a else False

    print(f"ACCOUNT A: {account_A["name"]}, a {account_A["description"]} from {account_A["country"]}")
    print(f"ACCOUNT B: {account_B["name"]}, a {account_B["description"]} from {account_B["country"]}")

    guess = input(f"Who do you think has more followers. Type A or B (A/B)?\n {account_A["name"]}{vs}{account_B["name"]}")
    
    if guess.lower() == "b" and b_is_bigger == True:
        print("YOU GUESSED right")
        correct_guess += 1
        print("Correct guesses for now:", correct_guess)
        play(account_B, random.choice(data))
    else:
        print("You guessed wrong\n")
        print("Total correct guesses:", correct_guess)
        new_game()
    pass
mygame = higher_lower()




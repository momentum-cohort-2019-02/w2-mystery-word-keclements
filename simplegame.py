import random  #important is command

def playgame():
    alphabit = ["a","b","c"]  #define variable
    random_letter = random.choice(alphabit) 
    letter_pick = input("What is your letter guess")
    if letter_pick == random_letter:
        print("you are right")
    else:
        print("wrong")
    return

playgame() 

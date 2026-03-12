"""This is to play matches in the terminal. The score will also be added and the game will end when you write something else other than rock paper or scissor and it will give you the score"""

import random

your=0
bot=0
l=["Rock","Paper","Scissor"]

while True:
    s=input("Me: ")
    a=random.choice(l)
    s=s.lower()
    if s=="rock" or s=="paper" or s=="scissor":
        print(f"Bot: {a}")
        if s=="rock":
            if a=="Rock":
                print("Draw")
            elif a=="Paper":
                print("I won")
                bot+=1
            elif a=="Scissor":
                print("You won")
                your+=1
            else:
                print("There's a problem")
        elif s=="paper":
            if a=="Rock":
                print("You won")
                your+=1
            elif a=="Paper":
                print("Draw")
            elif a=="Scissor":
                print("I won")
                bot+=1
            else:
                print("There's a problem")
        elif s=="scissor":
            if a=="Rock":
                print("I won")
                bot+=1
            elif a=="Paper":
                print("You won")
                your+=1
            elif a=="Scissor":
                print("Draw")
            else:
                print("There's a problem")
    else:
        print(f"The game ends\nScore:\nMy: {your}, Bot: {bot}")
        break

  """I tested it and lost so bad :( by 3-8"""

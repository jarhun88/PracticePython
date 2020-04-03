# Rock Paper Scissors

import random


def start():
    choices = ["rock", "paper", "scissors"]
    selection = random.choice(choices)
    hand = input("rock, paper, scissors?")
    while True:
        if hand == selection:
            return("Tie")
                
        elif hand == "rock":
            if selection == "paper":
                return ("Computer chose Paper! Computer wins!")
            else:
                return("Computer chose scissors! Player wins!")

        elif hand == "paper":
            if selection == "rock":
                return ("Computer Chose rock! Player wins!")
            else:
                return("Computer chose scissors! Computer wins!")
        elif hand == "scissors":
            if selection == "rock":
                return("Computer chose rock! Computer wins!")
            else:
                return("Computer chose paper! Player wins!")
        else:
            return("Please choose one of rock, paper, scissors.")


                
                      

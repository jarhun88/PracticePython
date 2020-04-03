# Cooperate vs Cheat
# An interactive game

import random
def start():
    you_score = 0
    comp_score = 0
    counter = 1
    
    print ("You have %d points. Computer has %d points." %(you_score, comp_score))
    first = input("Round %d: Cooperate or Cheat?" %(counter))

    good = "Cooperate"
    bad = "Cheat"
    choices = ["Cooperate", "Cheat"]

    random_comp = random.choice(choices)
    nice_comp = "Cooperate"
    mean_comp = "Cheat"
    types = [random_comp, nice_comp, mean_comp] #future additions = copycat, grudgebot, 
    computer = random.choice(types)

    coop_points = 2
    cheated_deduct = 1
    cheated_gains = 3

    while counter <= 5:
        if first == good:
            if computer == good:
                you_score = you_score + coop_points
                comp_score = comp_score + coop_points

                print ("Computer " + computer + "d!")
                print ("You have %d points. Computer has %d points." %(you_score, comp_score))
                counter += 1
                if counter <= 5:
                    first = input("Round %d: Cooperate or Cheat?" %(counter))
                    if computer == random.cstar:
                        computer = random.choice(choices)
                else:
                    print("Final Score: You have %d points. Computer has %d points." %(you_score, comp_score))

            elif computer == bad:
                you_score = you_score - cheated_deduct
                comp_score = comp_score + cheated_gains

                print ("Computer " + computer + "d!") 
                print ("You have %d points. Computer has %d points." %(you_score, comp_score))
                counter += 1
                if counter <= 5:
                    first = input("Round %d: Cooperate or Cheat?" %(counter))
                    if computer == random.choice(choices):
                        computer = random.choice(choices)
                else:
                    print("Final Score: You have %d points. Computer has %d points." %(you_score, comp_score))

        if first == bad:
            if computer == good:
                you_score = you_score + cheated_gains
                comp_score = comp_score - cheated_deduct

                print ("Computer " + computer + "d!")
                print ("You have %d points. Computer has %d points." %(you_score, comp_score))
                counter += 1
                if counter <= 5:
                    first = input("Round %d: Cooperate or Cheat?" %(counter))
                    if computer == random.choice(choices):
                        computer = random.choice(choices)
                else:
                    print("Final Score: You have %d points. Computer has %d points." %(you_score, comp_score))

            elif computer == bad:
                you_score = you_score 
                comp_score = comp_score

                print ("Computer " + computer + "d!")
                print ("You have %d points. Computer has %d points." %(you_score, comp_score))
                counter += 1
                if counter <= 5:
                    first = input("Round %d: Cooperate or Cheat?" %(counter))
                    if computer == random.choice(choices):
                        computer = random.choice(choices)
                else:
                    print("Final Score: You have %d points. Computer has %d points." %(you_score, comp_score))



                
                
        
               
               

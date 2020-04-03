import random



def dice_roll(sides=6):
    rolled_num = random.randint(1, sides)
    return rolled_num

def main():
    sides = 6
    rolling = True
    while rolling:
        ask = input("Ready to roll? ENTER = Roll, Q= Quit.")
        if ask != "q":
            rolled_num = dice_roll(sides)
            print ("You rolled a", rolled_num)
        else:
            rolling = False
    print ("goodbye")
   


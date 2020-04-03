# Character Input

def agemaster():
    name = input("What is your name?")
    age = int(input("What is your age?"))
    current_year = 2017
    year = str(100 - age + current_year)
    print (name + ", you will turn 100 in the year " + year)

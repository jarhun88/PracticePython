def which():
    number = input("Give a number!")
    if int(number) % 4 == 0:
        print ("This is a multiple of 4")
    elif int(number) % 2 == 0:
        print ("This number is even.")
    else:
        print ("This number is odd.")

def perfect():
    num = input("Give a number!")
    check = input("A second number!")
    if int(num) % int(check) == 0:
        print("Perfect division!")
    else:
        print("Imperfect like you!")

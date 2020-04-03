# Checking for prime numbers

def primer(help_text):
    return int(input(help_text))

check = primer("Give me a number: ")
if check % 2 != 0:
    print("That is a prime number!")
else:
    print("That is not a prime number!")

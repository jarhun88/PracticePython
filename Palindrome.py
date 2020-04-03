# String Palindrome detector

def test(str):
    # print (len(str))
    backwards = str[: : -1]
    if backwards == str:
        print ("This is a Palindrome!")
    else:
        print("This is not a Palindrome!")
        

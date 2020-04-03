def one_by_one(lst):
    for n in lst:
        if n < 5:
            print (n)

def less_than_5(lst):
    new_lst = []
    cond = input("Give your condition")
    for n in lst:
        if n < int(cond):
            new_lst.append(n)
    print (new_lst)

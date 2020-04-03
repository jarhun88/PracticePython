def lister(lst1, lst2):
    new_lst = []
    for n in lst1:
        if n in lst2:
            if n not in new_lst:
                new_lst.append(n)
    print (new_lst)

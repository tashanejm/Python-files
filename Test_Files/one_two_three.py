def one_two_three(n):
    # just do it!
    print(n*str(1))
    if n == 0: print(str(0)+", "+str(0))
    elif n <= 9 : print(str(n)+", "+n*str(1))
    else:
        ha = str(n)
        print(ha[1]*2+ha[0]+", " + n*str(1))
    return []

one_two_three(0)  

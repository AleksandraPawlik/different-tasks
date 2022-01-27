##Wyznacz największy wspólny dzielnik liczb a i b za pomocą algorytmu Euklidesa

def nwd(a, b):
    if a == 0 and b != 0:
        return b
    elif a != 0 and b == 0:
        return a
    else:
        if a < b:
            supp = a
            a = b
            b = supp

        while (a % b != 0):
            supp = a % b
            a = b
            b = supp

        return b




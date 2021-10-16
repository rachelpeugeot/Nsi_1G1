from math import*

def syracuse(n):
    """syracuse(n) retourne le nombre d'itérations de la suite de syracuse sur n int"""
    s = 0
    while n>1:
        s+=1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
    return s, True

def test_syracuse(n):
    """test_syracuse(n) verifie syracuse(n) est vrai de o au rang n int"""
    for i in range (n):
        if syracuse(n) == False:
            return False
    return True
        

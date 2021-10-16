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
    return s

def syracuse_verif(n):
    """syracuse_verif(n) verifie si n suit la suite de syracuse"""
    while n>1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
    if n == 1:
        return True
    else:
        return False
        
            

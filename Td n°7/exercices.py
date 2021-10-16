from math import*

def decbin(n):
    """decbin(n) retourne n décimal sous forme binaire"""
    liste = []
    while n>=1:
        if n%2 == 1:
            liste.append(1)
            n = n//2
        else:
            liste.append(0)
            n = n//2
    liste = reverse(liste)
    liste.pop()
    return liste

def reverse(liste):
    """reverse(liste) renvoie une liste inversée"""
    a = 0
    liste1 = []
    for i in range (len(liste)):
        a = liste.pop()
        liste1.append(a)
    return liste1

def bindec(liste):
    """bindec(liste) retourne le nombre décimal correspondant à la suite binaire"""
    liste = reverse(liste)
    dec = 0
    for i in range (len(liste)):
        if liste[i] == 1:
            dec = dec + 2**i
    dec = 2*dec
    return dec















        
        

from math import*
from random import*

def calendrier_janvier():
    """calendrier_janvier() retourne la liste des jours de janvier"""
    for i in range (1, 32):
        print(i, "janvier")

def diviseur(n):
    """diviseur(n) calcule et affiche les diviseurs de n entier et postif"""
    for i in range (1, n):
        if n%i == 0:
            print(i)

def dix_par_dix():
    """dix_par_dix() retourne un tableau de 10 colonnes sur 10 lignes donc chaque case est le produit de sa case et de sa colonne"""
    for i in range (10):
        for j in range (10):
            print(i*j, ",", end='')
        print()

def calendrier():
    """calendrier() retourne le calendrier d'une année"""
    for i in range (1, 13):
        if i == 4 or i == 6 or i == 9 or i == 11:
            for j in range (1, 31):
                print("jour", j, "mois", i)
        elif i == 2:
            for j in range (1, 30):
                print ("jour", j, "mois", i)
        else:
            for j in range (1, 32):
                print ("jour", j, "mois", i)
                
def multiple_commun(a, b, c):
    """multiple_commun(a, b, c) retourne True si c est un multiple commun de a et b et False sinon avec a, b, c int"""
    if c%a == 0 and c%b == 0:
        return True
    else:
        return False
    
def ppcm(a, b):
    """ppcm(a, b) retourne le ppcm de a et de b int """
    for i in range (a, b*a):
        if multiple_commun(a, b, i) == True:
            return i

def logarithme(n):
    """logarithme(n) retourne le nombre de fois où l'on divise n par 2 nécessaire pour arriver à un n<=1 et le n résultant"""
    s=0
    while n>1:
        n=n/2
        s+=1
    return s, n

def suite_h(l):
    """suite_h(l) retourne les l premiers termes de la suite h0=0, h(n+1)= hn + 1/n"""
    h=0
    for i in range (1, l+1):
        print(h)
        h=h+(1/i)

def suite_r(l):
    """suite_r(l) retourne les l premiers termes de la suite r0=0, r(n+1)= rn + (1/n**2)"""
    r=0
    for i in range (1, l+1):
        print(r)
        r=r+(1/i**2)
























    

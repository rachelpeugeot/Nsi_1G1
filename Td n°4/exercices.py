from math import*

def liste_entier(n):
    """liste_entier(n) retourne une liste d'entiers entrés par l'opérateur de longueur n int"""
    a = 0
    liste = []
    for i in range (n):
        a = int(input("entrer la valeur désirée "))
        liste.append(a)
    return liste

def pair_et_impair(liste1, liste2):
    """pair_et_impair(liste1, liste2) avec liste1et liste 2 de longueur égale retourne liste3
    dont les éléments d'indice pair sont ceux de liste1 et les éléments d'indice impair de liste2"""
    l=len(liste1)
    liste3=[]
    for i in range (l):
        if i%2 == 0:
            liste3.append(liste1[i])
        else:
            liste3.append(liste2[i])
    return liste3

def liste_inverse(liste):
    """liste_inverse(liste) retourne liste1 l'inverse de liste"""
    liste1=[]
    a=0
    for i in range (len(liste)):
        a=liste.pop()
        liste1.append(a)
    return liste1

def maximum_liste(liste):
    """maximum_liste(liste) retourne le maximum des elements de cette liste d'entiers déja définie"""
    a = 0
    for i in range (len(liste)):
        if liste[i]>a:
            a = liste[i]
    return a

def diviseur(n):
    """diviseur(n) calcule et affiche les diviseurs de n entier et postif"""
    s = 0
    for i in range (1, n):
        if n%i == 0:
            s += 1
            print(i)
    return "Le nombre de diviseurs est", s

numero=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
contact=["Marie", "Jeanne", "Luc", "Eve", "Jean", "Marc", "Victor", "Louis", "Louise", "Arnauld"]

def correspondance(n):
    """correspondance(n) retourne le n auquel correspond n ou permet de constater que le propriétaire de n n'est pas dans le répertoire"""
    n=numero.index(n)
    if n<len(contact):
        return contact[n]
    else:
        return "non attribué"


    
























        

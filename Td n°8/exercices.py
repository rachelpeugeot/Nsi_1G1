from math import*

lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nombre = [i for i in range (25)]

def coder_lettre(n):
    """coder_lettre(n) renvoie le rang dans l'alphabet de n"""
    a = 0
    a = lettre.index(n)
    return a

def decoder_lettre(n):
    """decoder_lettre(n) renvoie la lettre de rang n de l'alphabet"""
    return lettre[n]

def decodage(msg):
    """decodage(msg) prend en argument une chaine de charactères et renvoie les possibilités de décodage de celui-ci"""
    liste = []
    for carac in msg:
        liste.append(carac)
    liste1 = []
    for i in range (25):
        for j in range (len(liste)):
            a = coder_lettre(liste[j])+i
            if a>24:
                a = a-24
            a = decoder_lettre(a)
            liste1.append(a)
        print("possibilité ", i, liste1)
        liste1 = []

def strlist(msg):
    """strlist(msg) retourne str en liste"""
    liste = []
    for carac in msg:
        liste.append(carac)
    return liste
    
def liststr(liste):
    msg = "".join(liste)
    return msg


def compteur_e(msg):
    """compteur_e(msg) compte le nombre de e dans msg str"""
    s = 0
    msg = strlist(msg)
    for i in range (len(msg)):
        if msg[i]=="e":
            s+=1
    return s

def supprimer_e(msg):
    """supprimer_e(msg) renvoie msg sans les e"""
    msg = strlist(msg)
    for i in range (len(msg)):
        if msg[i]=="e":
            msg[i]=" "
    msg = liststr(msg)
    return msg
        










        

from math import*

def farheneitEncelsius(n):
    """frenheitEncelsius(n) convertit la température n en farenheit en celsius"""
    n=((n-32)*5)/9
    n=int(n)
    return n

def volume_cylindre(r, h):
    """volume_cylindre(r, h) prend en argument r le rayon et h la hauteur d'un cylindre et retourne le volume de ce cylindre"""
    v = 0
    v = (r**2)*pi*h
    v = int(v)
    return v

def divisible(a, b):
    """divisible(a, b) teste si a int est divisible par b int"""
    if a%b == 0:
        return True
    else:
        return False

def nb_premier(n):
    """nb_premier(n) retourne si n int est premier"""
    for i in range (2, n):
        if n%i == 0:
            return False
    return True

couleurs = ["blue", "green", "yellow", "red"]
def couleur(n):
    """couleur(n) renvoie la couleur correspondante à n"""
    return couleurs[n]

def échanger(a, b):
    """échanger(a, b) échange a et b"""
    a, b = b, a
    return a, b

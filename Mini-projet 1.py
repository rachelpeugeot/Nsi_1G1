from math import*

lettre=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "st", "u", "v", "w", "x", "y", "z"]
nombre=[i for i in range (25)]

def coder(x):
    """coder(x) retourne le rang dans l'alphabet de la lettre x"""
    return lettre.index(x)

def decoder(x):
    """decoder(x) retourne la lettre de rang x int"""
    return lettre[x]

def encoder(liste, x):
    """encoder(liste, x) retourne une lettre x codée avec le code de césar donnée en liste"""
    v=0
    v=lettre.index(x)
    return liste[v]

def cesar(x):
    """cesar(x) retourne l'alphabet avec le décalage x int"""
    liste=[]
    u=0
    v=""
    for i in range (25):
        u=i+x
        if u>24:
            u=u-25
        v=decoder(u)
        liste.append(v)
    return liste
    
def coder_message(message, x):
    """coder_message(msg, x) retourne msg avec des espaces str codé avec le décalage x int"""
    liste2=[]
    for carac in message:
        liste2.append(carac)
    final=" "
    l=len(msg)
    liste=cesar(x)
    dcd=[]
    for i in range (l):
        v=encoder(liste, msg[i])
        dcd.append(v)
    final=' '.join(dcd)
    return dcd
        
    
    
    

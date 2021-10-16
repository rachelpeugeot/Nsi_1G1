from math import*

"""exercice 1, 2"""
def bataille_navale(a, b):
    """bataille_navale(a, b) retourne durant 10 tours une bataille navale avec a et b la localisation du bateau"""
    for i in range (10):
        x = int(input("entrer la colonne choisie "))
        y = int(input("entrer la ligne choisie "))
        if x == a and y == b:
            return "Coulé"
        else:
            if (x == a and y == b-1) or (x == a and y == b+1) or (x == a-1 and y == b) or (x == a+1 and y == b):
                print("En vue")
            else:
                print("A l'eau")

def second_degré():
    """second_degré() retourne à l'utilisateur si le trinôme a des racines, combien et le cas échéant leur(s) valeur(s)"""
    a = int(input("entrer le coefficient a tel que ax**2 "))
    b = int(input("entrer le coefficient b tel que bx "))
    c = int(input("entrer le coefficient c tel que c "))
    d = (b**2)-(4*a*c)
    if d > 0:
        d = sqrt(d)
        x1 = (-b+d)/(2*a)
        x2 = (-b-d)/(2*a)
        return "Le trinôme a deux solutions ", x1," et ", x2
    elif d == 0:
        x0 = (-b)/(2*a)
        return "Le trinôme a une solution ", x0
    else:
        return "Le trinôme n'a pas de solutions."

def réunion(a):
    """réunion(a) indique les personnages compatibles avec a"""
    if a == "Marie":
        return "Marc, Janine, Luc"
    elif a == "Jean":
        return "Janine"
    elif a == "Janine":
        return "Marie, Marc, Luc"
    elif a == "Marc":
        return "Marie, Janine, Jean"
    else:
        return "Marie, Marc, Janine"














    
        

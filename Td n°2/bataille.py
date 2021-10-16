a=4
b=7
print("Vous avez 5 essais")

i = 0
while i < 5:
    print("A vous de jouer")
    x=int(input("Entrer le numéro de ligne "))
    y=int(input("Entrer le numéro de colonne "))
    if x==a and y==b :
        print("Coulé")
        i=5
    else :
        if (x==a and y==b+1) or (x==a and y==b-1) or (y==b and x==a-1) or (y==b and x==a+1):
            print("En vue")
        else :
            print("A l'eau")
    i=i+1



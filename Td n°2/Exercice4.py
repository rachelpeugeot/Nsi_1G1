from math import*
##Ce programme permet de savoir avec qui on peut inviter un individu a##
print("ce programme indique les compatibilités entre les individus invités à un diner")
a=input("Qui vient au diner ? ")

jean="jean"
marc="marc"
janine="janine"
luc="luc"
marie="marie"

jean==True
janine==True
luc==True
marie==True
marc==True

for i in range (1):
    if a==jean:
        marie==False
    elif a==marie:
        jean==False
    elif a==janine:
        luc==False
    elif a==luc:
        jean==False
    else:
        marc==True
    if marie==True:
        print("marie")
    if marc==True:
        print("marc")
    if jean==True:
        print("jean")
    if janine==True:
        print("janine")
    if luc==True:
        rint("luc")
    
    
    

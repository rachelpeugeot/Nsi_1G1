from math import*

a=float(input("rentrer la valeur de a "))
b=float(input("rentrer la valeur de b "))
c=float(input("rentrer la valeur de c "))

delta=(b**2)-(4*a*c)

if delta<0:
    print("Le polynôme n'a pas de racines")
elif delta==0:
    xzero=-b/(2*a)
    print("Le polynôme a une racine double, " ,xzero)
else:
    d=sqrt(delta)
    xun=(-b+d)/(2*a)
    xdeux=(-b-d)/(2*a)
    print("Le polynôme a deux racines, ",xun," et ",xdeux)
    
    


    

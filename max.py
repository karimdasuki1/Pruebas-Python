
n1=input("ingresa n1")
n2=input("ingresa n2")

def max (n1, n2):
    if n1 < n2:
        print (n2)
    elif n2 < n1:
        print (n1)
    else:
        print ("Son iguales")


max(n1, n2)

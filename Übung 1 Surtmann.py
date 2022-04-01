intVar = 0
floatPi = 0
summe = 0

strTerme = input(" Anzahl der Therme eingeben: ")
intTerme = int(strTerme)

while intVar <= intTerme:
    
    floatPi = (((-1)**intVar) / (2*intVar + 1))
    summe += floatPi
    intVar += 1
    
print("Die Annäherung an Pi beträgt: ", summe*4)
    

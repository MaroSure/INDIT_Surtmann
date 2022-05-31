eing1 = float(input("Eingabe 1 Zahl: ")) 

eing2 = float(input("Eingabe 2 Zahl: ")) 


def summe(eing1, eing2):      
    zwischensumme = eing1 + eing2
    return (zwischensumme)


def differenz(eing1, eing2):      
    zwischendifferenz = eing1 - eing2
    return (zwischendifferenz)


def produkt(eing1, eing2):      
    zwischenprodukt = eing1 * eing2
    return (zwischenprodukt)

def quotient(eing1, eing2):
    if eing2 == 0:
        print("Division durch 0")
        return
    zwischenquotient = eing1 / eing2
    return (zwischenquotient)

Wert1 = summe(eing1, eing2)
Wert2 = differenz(eing1, eing2)
Wert3 = produkt(eing1, eing2)
Wert4 = quotient(eing1, eing2)

print("Summe: ", Wert1)
print("Differenz: ", Wert2)
print("Produkt: ", Wert3)
print("Quotient: ", Wert4)

Namen = ["Max", "Isabella", "Kev", "Florian", "Marco"] # Liste.


def Begrueßung(name):
    print("Hallo ", name) # Ausgabe
    print("Schön dich zu sehen!") 
    print("Viel Spaß!") 
    return # Rückgabe 

def Begrueßung2(namensliste): 
    for ein_name in namensliste: # Schleife
        
        print("Hallo ", name, "!") 
        print("Schön dich zu sehen!") 
        print("Viel Spaß mit dem Programm!") 
    return


print("Version 1:") 
for name in Namen:  
    Begrueßung(name)
    

print("") # Ausgabe (dient nur als Absatz)
    

print("Version 2:") 
Begrueßung2(Namen)
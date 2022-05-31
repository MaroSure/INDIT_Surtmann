mein_woerterbuch = {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon","pfirsich":"peach"}


print("Wählen Sie eine Funktion: ")

print("[A] = Wortabfrage")

print("[H] = Wort hinzufügen")

correct = False
    
while correct == False: 
    
    eingabe = input("Auswahl Funktion: ") 
    if eingabe == "A":
                                        
        wort=input("Wort in Deutsch: ")
        wort = wort.lower() 
        if wort in mein_woerterbuch:
            print("Wort in English: ",mein_woerterbuch[wort]) 
        else:
            print('Nicht vorhanden')
    
    elif eingabe == "H":
        print("Eingabe nur in Kleinbuschstaben!",)   
        mein_woerterbuch[input('Wort in Deutsch:')] = input('Wort in English:') 
          
    
    else:
        print("Nicht bekannt")
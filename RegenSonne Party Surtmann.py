#Regen oder Sonne bei Party                                                                Info: == bedeutet Vergleichsoperator 
 
wetter = input("Wochenendwetter - 'SONNE' oder 'REGEN'?" )

if wetter.upper() == "SONNE":
    print("Party im Garten")
    
elif wetter.upper() == "REGEN":
    print("Party im Keller")
    
else:
    print("geben Sie 'SONNE' oder 'REGEN' ein")
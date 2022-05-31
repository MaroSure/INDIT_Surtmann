
import math

def eingabe():
    
    correct = False
    while correct == False:
        radius = input("Eingabe Radius: ")
        try: 
            rad = float(radius)     
            if rad > 0:
                correct = True                
            else:
                print("Zahl ungültig!! (Zahl muss positiv sein!) ")
        except ValueError:
            print("Eingabe ungültig!! (Zahl muss positiv sein!)")
    return rad

def kreisumfang(radius):
    umfang = 2*radius*math.pi
    return umfang


kreisradius = eingabe()
print("Eingegebener Radius: ", kreisradius)


umfang = kreisumfang(kreisradius)
print("Kreisumfang beträgt: ", umfang)
#Übung 2
#Programm, das in 10 Grad Schritten zwischen 0 und 180Grad den jeweils cos-Wert berechnet und ausgibt.

import math
winkel_grad = 0

while winkel_grad <= 180:
    winkel_rad = winkel_grad * math.pi / 180
    cosinus = math.cos(winkel_rad)
    print("winkel : ", winkel_grad, "-> cosinus: ", cosinus)
    winkel_grad+=10 
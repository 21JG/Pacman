from math import cos
from math import sin

"""Jarod Herrera herrerajarod@gmail.com"""
"""Descripcion se lee los inputs leemos la altura de la honda,luego las
   posiciones donde comienza y donde acaba y por ultimo el numero de intentos, 
   luego como un ejercicio de cinematica tomamos la velocidad inicial en 
   x y en y y los asociamos a su respectivo angulo y su correspondiente cos para x
   y sen para luego tomamos la formula de altura maxima en tiro vertical y luego 
   para ver la velocidad final en y usamos la formula , finalmente tomamos los 
   tiempos de vuelo inicial , tiempo de vuelo final , el tiempo final y luego 
   evaluamos el tiempo total usado y este lo multiplicamos por el vox para saber
   la posicion final en x ya por ultimo si el result esta dentro de los puntos es
    duck de lo contrario es nuck."""

pi =  3.14159
g = 9.80665

while True:
    try:
        h = float(input())
        p1,p2 = map(int,input().split())
        n = int(input())

        for tries in range(n):
            angle,vo = map(float,input().split())
            angle = angle * pi / 180
            vox= vo * cos(angle)
            voy= vo * sin(angle)
            hMax = (voy**2)/(g*2)+h
            vfy = pow(2*g*hMax,1/2)
            tv = voy / g
            tf = vfy / g
            tt = tv + tf
            fp = vox * tt
            r =round(fp,5)
            if (p1 < r < p2): print(fp, " -> DUCK ")
            else:print(fp, " -> NUCK ")
    except EOFError:
        break

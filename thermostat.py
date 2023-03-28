
"""Jarod Herrera herrerajarod@gmail.com"""
"""Descripcion se los inputs de en que temperatura esta y a cual debe llegar a,b
    l es la temperatura maxima por la que puede estar , r es la temperatura minima 
    a la que puede llegar y la minima variacion de temperatura es x ,entonces primero
    evauluo si la temperatura esperada es igual a la que se debe llegar ,el valor
    absoluto entre la diferencia de a y b debe ser mayor o igaul a la minima variacion,
    luego se evalua si el vlr minimo de temperatura es menor al valor maximo entre a y b
    o si el valor minimo entre a y b y el valor es menor a al valor de temperatura , y luego
    realiza el mismo proceso con cambiando r y p pero que se cumplan esta vez ambos statments
    por ultimo imprimir"""


n=int(input())
list=[]


for i in range(n):

    l,r,x = map(int,input().split())
    a,b = map(int,input().split())

    p=min(a,b)
    j=max(a,b)
    f=abs(a - b)

    if a==b:
        list.append(0)
    elif f>=x:
        list.append(1)
    elif r-p >=x and j-l >=x:
        list.append(3)
    elif r-j>= x or p-l>=x:
        list.append(2)
    else:
        list.append(-1)

for n in list:
        print(n)

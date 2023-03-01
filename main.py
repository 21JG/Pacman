import sys
"""Jarod Herrera herrerajarod@gmail.com"""
"""Descripcion se lee el input ,luego se crean dos ciclos for 
    uno para el row o el path par y otra para el impar ya que lee
     de distinta manera uno de izquierda a derecha y el otro en 
     sentido contrario luego valida si es un fantamsa para finalizar
     contador temporal o si es comida para sumarle 1 al contador temporal
     por ultimo se valida que no quede el registro del temporal mayor al 
     del contador"""


n=int(input())
list=[]
contador=0
temp=0

for line in range(n):
    inputText = input()
    if len(inputText) == n:
        list.append(inputText)


for path in list:
    if list.index(path) % 2 == 0:
        for character in path:
            if character == 'A':
                if contador < temp:
                    contador=temp
                temp=0

            elif character == 'o':
                temp=temp+1

        #procedure to odd position

    else:
        # procedure to even
        for position in range(len(path)):
            length = len(path)-1
            character = path[length-position]
            if character == 'A':
                if contador < temp:
                    contador = temp
                temp = 0

            elif character == 'o':
                temp = temp + 1
if temp > contador:
    contador = temp

print(contador)



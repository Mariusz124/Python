from random import randint


los = randint(1,10)
odp = -1
i = 0
while odp!= los:
    i+=1
    odp = int(input('podaj liczbę z zakresu  1 - 10: '))
    if odp > los:
        print('Podana liczba jest za duża')
    elif odp < los:
         print('Podana liczba jest za mała ')
print('Brawo ! wygrałeś za:',i,'razem !')



while True:
    print('___Kalkulator___')
    print(' 1.Dodawanie')
    print(' 2.Odejmowanie')
    print(' 3.Iloczyn')
    print(' 4.Dzielenie')

    a= int(input('Podaj pierwszą wartość: '))
    b= int(input('Podaj drugą wartość: '))

    dzialanie = input('Wybierz działanie ')

    if dzialanie == '1':
        print(f'{a}+{b}=',a+b)
    elif dzialanie == '2':
        print(f'{a}-{b} =',a-b)
    elif dzialanie == '3':
        print(f'{a}*{b} =',a*b)
    elif dzialanie == '4':
        try:
            print(f'{a}/{b}=',a/b)
        except ZeroDivisionError:
            print('nie dzielimy przez 0!')
    else:
        print('nie ma takiej opcji')
    answer = input('Czy chcesz zakonczyc działanie  (t? oznacza "tak", n oznacza "nie"')
    if answer == 't':
        break
    if answer =='n':
        continue





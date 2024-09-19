
# def even_odd_vending(num):
#     if (num%2)==0:
#         print('Liczba jest parzysta')
#     else:
#         print('Liczba jest nieparzysta')
#         count = 1
#     while count<=9:
#          num+=2
#          print(num)
#          #inkrementacja liczby wyswietlanych liczb
#          count+=1
# if __name__ == '__main__':
#      try:
#          num= float(input('Wpisz liczbe całkowita: '))
#          if num.is_integer():
#              even_odd_vending(int(num))
#          else:
#              print('Prosze wpisac liczbe całkowita')
#      except ValueError:
#         print('Prosze wpisac liczbe całkowita')


'''
s = "abcfdefghgfhghgkhjkhj0987654321+#$%^&*ABCDEFGHIJKLMNOP"
dlugosc_hasla = 7
haslo = "".join(random.sample(s,dlugosc_hasla))
print(haslo)
'''
# Totolotek!
import random
wszystkie_liczby =[]

for i in range(1,50):
    wszystkie_liczby.append(i)
random.shuffle(wszystkie_liczby)
wylosowane_liczby = []
for i in range(1,7):
    wybrana_liczba=random.randrange(0,len(wszystkie_liczby),1)
    wylosowane_liczby.append(wszystkie_liczby[wybrana_liczba])
    wszystkie_liczby.pop(wybrana_liczba)
print(wylosowane_liczby)
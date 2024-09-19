'''
Wizualizacja  tygodniowych wydatkow przy uzyciu wykresu słupkowego
'''
import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    # liczba słupków
    num_bars = len(data)
    # Ta lista zawiera punkty na osi Y, które będa określać
    #środek poszczególnych słupków. W naszym przypadku będą to liczby [1,2,3...]
    positions = range(1,num_bars+1)
    plt.barh(positions,data, align='center')
    # Ustawiamy etykiety dla poszczególnych słupków
    plt.yticks(positions,labels)
    plt.xlabel('kwota')
    plt.ylabel('Kategorie')
    plt.title('Tygodniowe wydatki')
    # Włączamy siatkę, która moze nam pomóc w wizualnej analizie wykresu
    plt.grid()
    plt.show()

if __name__ == '__main__':
    n = int(input('Podaj liczbę kategori:'))
    labels = []
    expenditures = []
    for i in range(n):
        category = input('podaj kategorie:')
        expenditure = float(input('Wydatki:'))

        labels.append(category)
        expenditures.append(expenditure)
    create_bar_chart(expenditures,labels)




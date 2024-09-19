import matplotlib.pyplot as plt


def create_bar_chart(data, labels):
    #liczba słupków
    num_bars = len(data)
    # Ta lista zawiera punkty na osi y, gdzie znajdzie sie srodek kazdego
    # ze słupków. W naszym przypadku beda to wartosci [1,2,3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    #Ustawiene etykiety poszczególnych słupków
    plt.yticks(positions, labels)
    plt.xlabel('Liczba kroków')
    plt.ylabel('Dzień tygodnia')
    plt.title('Zestawienie liczb wykonanych kroków')
    # Wyswietlenie siatki która moze pomóc w porównaniu wartosci

    plt.show()

if __name__ == '__main__':
    # Liczba kroków jakie wykonałem kazdego dnia w zeszłym  tygodniu
    steps = [7000, 8900, 1078, 3467, 11045, 5095, 6534]
    # Nazwy dni odpowiadajace liczbie kroków
    labels = ['pon','wto', 'sro', 'czw','pia', 'sob', 'nie']
    create_bar_chart(steps, labels)
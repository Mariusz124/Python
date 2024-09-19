def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    #Znajdujemy medianę
    if N % 2 == 0:
        # jesli N jest parzyste
        m1 = N/2
        m2 = (N/2) + 1
        # Konwertujemy na liczbę całkowitą i przeliczamy na indeksy
        m1 = int(m1) -1
        m2 = int(m2) -1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # Konwertujemy na liczbę całkowita i przeliczamy na indeks
        m = int(m) - 1
        median = numbers[m]
    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calculate_median(donations)
    N = len(donations)
    print('Mediana sumarycznych kwot datkow z ostatnich {0} dni jest {1} zł.'.format(N, median))
from collections import Counter
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    #Obliczamy srednia
    mean = s/N

    return mean
def find_differences(numbers):
    # Obliczamy średnia
    mean = calculate_mean(numbers)
    # Obliczamy róznice od sredniej
    diff = []
    for num in numbers:
        diff.append(num-mean)

    return diff
def calculate_variance(numbers):
    # Wyznaczamy liste różnic
    diff = find_differences(numbers)
    # Obliczamy kwadraty różnic
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
        # Obliczamy wariancje
        sum_squared_diff = sum(squared_diff)
        variance = sum_squared_diff/len(numbers)
        return variance

if __name__ =='__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('Wariancja listy liczb wynosi {0}'.format(variance))
    std = variance**0.5
    print('Odchylenie standardowe listy liczb wynosi {0}'.format(std))

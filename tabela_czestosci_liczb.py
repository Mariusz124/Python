from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('liczba   Czestosc')
    for number in numbers_freq:
        print('{0}  {1}'.format(number[0], number[1]))

if __name__== '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)

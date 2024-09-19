
def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
    print('suma licz z pliku wynosi: {0}'.format(s))

if __name__ == '__main__':
    sum_data('mydata.txt')





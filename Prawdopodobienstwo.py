from sympy import FiniteSet
import random
import matplotlib.pyplot as plt
'''''
def probability(space, event):
    return len(event)/len(space)

def check_prime(number):
    if number !=1:
        for factor in range(2, number):
            if number % factor ==0:
                return False
    else:
        return False
    return True
if __name__ == '__main__':
    space = FiniteSet(*range(1,21))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)
    print('Przestrzen próbek losowych :{0}'.format(space))
    print('zdarzenie: {0}'.format(event))
    print('Prawdopodobienstwo wyrzucenia liczby pierwszej:{0:.5f}'.format(p))
'''''

targer_score = 20

def roll():
    return random.randint(1,6)

if __name__ == '__main__':
    score =0
    num_roll = 0

    while score < targer_score:
        die_roll = roll()
        num_roll +=1
        print('Liczba oczek {0}'.format(die_roll))
        score += die_roll

    print('Sume {0} oczek uzyskano w {1} rzutach kostką.'.format(score, num_roll))




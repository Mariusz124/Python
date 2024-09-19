import matplotlib.pyplot as plt
import numpy as np
import csv

# costs = ['jedzenie','rozrywka','czynsz', 'odzież']
# pln = [450,1200,900,650]
# explode = [0,0,0.2,0]
# plt.pie(pln,labels=costs,shadow=True, startangle=90,explode=explode)
# plt.show()
x , y =[],[]
with open('dane.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y,label='Dane')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



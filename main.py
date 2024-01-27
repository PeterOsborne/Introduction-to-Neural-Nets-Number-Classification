import numpy as np
import random as rand
import csv

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range (100):
        num = rand.randint(0,100)
        even = 0 if (num % 2 == 0) else 1
        writer.writerow([num, even])
        i+=1

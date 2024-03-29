import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

#filename = os.path.join(dir_path, 'input_test.txt')
filename = os.path.join(dir_path, 'input.txt')
lista = get_input_str(filename)

priority = 0
for rucksack in lista:
    first, second = rucksack[ : len(rucksack) // 2], rucksack[len(rucksack) // 2 : ]
    d = dict()
    for item in first:
        d[item] = (ord(item) - 33) % 58 - 5
    for item in second:
        if item in d:
            priority += d[item]
            break

print(priority)
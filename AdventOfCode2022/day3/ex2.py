import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

#filename = os.path.join(dir_path, 'input_test.txt')
filename = os.path.join(dir_path, 'input.txt')
lista = get_input_str(filename)

priority = 0
for i in range(0, len(lista), 3):
    d = dict()
    d2 = dict()
    for item in lista[i]:
        d[item] = (ord(item) - 33) % 58 - 5
    for item in lista[i+1]:
        if item in d:
            d2[item] = d[item]
    for item in lista[i+2]:
        if item in d2:
            priority += d2[item]
            break

print(priority)
import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

#filename = os.path.join(dir_path, 'input_test.txt')
filename = os.path.join(dir_path, 'input.txt')
list = get_input_str(filename)

priority = 0
for rucksack in list:
    first, second = rucksack[ : len(rucksack) // 2], rucksack[len(rucksack) // 2 : ]
    d = dict()
    for item in first:
        if item.islower():
            d[item] = ord(item) - 96
        else:
            d[item] = ord(item) - 38
    for item in second:
        if item in d:
            priority += d[item]
            break

print(priority)
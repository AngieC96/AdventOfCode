import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

filename = os.path.join(dir_path, 'input.txt')
list = get_input_str(filename)

inventory = 0
food = []
for calories in list:
    if calories != '':
        inventory += int(calories)
    else:
        food.append(inventory)
        inventory = 0

first = max(food)
food.remove(first)
second = max(food)
food.remove(second)
print(first + second + max(food))
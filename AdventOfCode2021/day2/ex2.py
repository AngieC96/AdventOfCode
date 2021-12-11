import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str_int

filename = os.path.join(dir_path, 'input.txt')
instructions = get_input_str_int(filename)

position, depth, aim = 0, 0, 0
for instruction in instructions:
    if instruction[0] == 'forward':
        position += instruction[1]
        depth += aim * instruction[1]
    elif instruction[0] == 'down':
        aim += instruction[1]
    elif instruction[0] == 'up':
        aim -= instruction[1]
print(position * depth)
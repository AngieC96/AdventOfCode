import os, sys
# importing "array" for array creations
import array as arr

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

filename = os.path.join(dir_path, 'input.txt')
report = get_input_str(filename)

l = len(report)
b = len(report[0])

bites = arr.array('I', [0] * b)
for line in report:
    for i, c in enumerate(line):
        bites[i] += int(c)

# Transform the sum in binary number as requested
gamma = ''
for i in bites:
    if int(i) > l/2:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)

# Compute the 1's complement of gamma
# https://www.tutorialspoint.com/find-one-s-complement-of-an-integer-in-cplusplus
ones = ((1 << b) - 1) # ((2**l) - 1)
epsilon = ones ^ gamma # bitwise xor

power_cons = gamma * epsilon
print(power_cons)
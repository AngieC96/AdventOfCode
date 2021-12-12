import os, sys
# importing "array" for array creations
import array as arr

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

filename = os.path.join(dir_path, 'input.txt')
report = get_input_str(filename)

l = len(report[0])
if len(report) > 16:
    print(f"This method doesn't work if the number of lines ({len(report)}) is greater than 16")
    exit()

# Sum all the bits column-wise: I know then number of 1's in every column
sum = 0
for line in report:
    sum += int(line, 16)

# Transform the sum in binary number as requested
gamma = ''
for i in hex(sum)[2:]:
    if int(i) > l:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)

# Compute the 1's complement of gamma
# https://www.tutorialspoint.com/find-one-s-complement-of-an-integer-in-cplusplus
ones = ((1 << l) - 1) # ((2**l) - 1)
epsilon = ones ^ gamma # bitwise xor

power_cons = gamma * epsilon
print("power_cons", power_cons)
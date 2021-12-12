import os, sys
# importing "array" for array creations
import array as arr

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

filename = os.path.join(dir_path, 'example.txt')
report = get_input_str(filename)

l = len(report[0])
if l > 16:
    print(f"This method doesn't work if the length of a row ({l}) is greater than 16")
    exit()

sum = 0
for line in report:
    sum += int(line, 16)
print("bitwise sum", hex(sum))

gamma = ''
for i in hex(sum)[2:]:
    if int(i) > l:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)
print("gamma", gamma)

# It is the 1's complement of gamma
# Flip every bit:
epsilon = ~gamma
# Adding 2^l to convert signed to unsigned integer:
epsilon = epsilon + 2**l # + (1 << l)
print("epsilon", epsilon, bin(epsilon), int(bin(epsilon), 2))

# It is the 1's complement of gamma
# https://www.tutorialspoint.com/find-one-s-complement-of-an-integer-in-cplusplus
ones = ((1 << l) - 1) # ((2**l) - 1)
epsilon2 = ones ^ gamma # bitwise xor
print("epsilon", epsilon2, bin(epsilon2), int(bin(epsilon2), 2))

power_cons = gamma * epsilon
print("power_cons", power_cons)
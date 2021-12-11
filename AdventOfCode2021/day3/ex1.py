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
gamma = int('10110', 2)
gamma2 = int('10101', 2)
print(gamma, bin(gamma))
print(bin(gamma + gamma2))

sum = 0
for line in report:
    sum += int(line, 16)
print(hex(sum))

gamma = ''
for i in hex(sum)[2:]:
    if int(i) > l:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)
print(gamma)

# Links:
# - https://superuser.com/questions/975684/converting-negative-decimal-to-binary
# -

print("\nEpsilon")
# It is the 1's complement of gamma
epsilon = ~gamma
print(epsilon, bin(epsilon), int(bin(epsilon), 2))
print(bin(-epsilon), int(bin(-epsilon), 2))
print(gamma + epsilon, bin(gamma + epsilon))
# Adding 2^l to convert signed to unsigned integer
epsilon = epsilon + 2**l
print(epsilon, bin(epsilon), int(bin(epsilon), 2))

# It is the 1's complement of gamma
# https://www.tutorialspoint.com/find-one-s-complement-of-an-integer-in-cplusplus
ones = ((1 << l) - 1)
epsilon2 = ones ^ gamma
print(epsilon2, bin(epsilon2), int(bin(epsilon2), 2))
print(bin(ones), bin(1 << l), bin(2**l))

power_cons = gamma * epsilon
print(power_cons)

print(" ", 441, bin(441))
print(-441, bin(-441))
print(-441, " ", bin(-441 ^ ((1 << 9) - 1)))
print(" ", 441, " ", bin(441 ^ ((1 << 9) - 1) + 1))

print("\n\n")
print("5", bin(5))
print("-5", bin(-5))
print("~5", bin(~5)) # It doesn't flip the numbers!
print("~5+1", bin(~5+1)) # It yields the right 2's complement
print("1's complement", bin(5 ^ ((1 << 3) - 1)))
print("2's complement", bin(5 ^ ((1 << 3) - 1) + 1), 5 ^ ((1 << 3) - 1) + 1) # WRONG! You cannot flip the sign bit
print(5 ^ ((1 << 3) - 1) + (1 << 7))
print(2**7+2)

print("\nSizes:")
print(sys.getsizeof(0)) # It has 24 bytes of overhead: every number is an object, so it has a very large size in memory
print(sys.getsizeof(5 ^ ((1 << 3) - 1))) # (28 - 24 = ) 4 bytes = 32 bits to memorize this number
print(sys.getsizeof(5 ^ ((1 << 3) - 1) + (1 << 31))) # (32 - 24 =) 8 bytes = 64 bits
print(sys.getsizeof(5 ^ ((1 << 3) - 1) ^ (1 << 31)))

# https://www.kite.com/python/answers/how-to-take-two's-complement-in-python
print("\nFixed bits numbers")
number = 5
binary_number = int("{0:08b}".format(number))
print(binary_number, str(binary_number))
flipped_binary_number = ~binary_number
flipped_binary_number = flipped_binary_number + 1
str_twos_complement = str(flipped_binary_number)
print(flipped_binary_number, type(flipped_binary_number), str_twos_complement, type(str_twos_complement))
twos_complement = int(str_twos_complement, 2)
print(twos_complement, str_twos_complement)
twos_complement2 = bin(binary_number ^ ((1 << 8) - 1) + 1) # ?!?!?!?!?
print(twos_complement2)
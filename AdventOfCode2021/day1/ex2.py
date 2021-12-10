import os, sys
dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_int

filename = os.path.join(dir_path, 'input.txt')
measurements = get_input_int(filename)

sum_three_measurements = []
for i in range(2, len(measurements)):
    sum_three_measurements.append(measurements[i] + measurements[i - 1] + measurements[i - 2])

count = 0
for i in range(1, len(sum_three_measurements)):
    if sum_three_measurements[i] > sum_three_measurements[i - 1]:
        count += 1
print(count)

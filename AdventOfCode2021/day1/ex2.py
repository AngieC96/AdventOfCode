import os, sys
dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_int

filename = os.path.join(dir_path, 'input.txt')
measurements = get_input_int(filename)

count = 0
previous_sum = sum(measurements[:3])
for i in range(2, len(measurements)):
    sum_three_measurements = sum(measurements[i - 3:i])
    if sum_three_measurements > previous_sum:
        count += 1
    previous_sum = sum_three_measurements
print(count)

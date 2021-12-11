import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_int

filename = os.path.join(dir_path, 'input.txt')
measurements = get_input_int(filename)
count = 0
for i in range(1, len(measurements)):
    if measurements[i] > measurements[i - 1]:
        count += 1
print(count)

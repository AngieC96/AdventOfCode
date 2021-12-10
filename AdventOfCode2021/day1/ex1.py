with open('input.txt') as file:
    lines = file.readlines()
    lines = [int(line.strip()) for line in lines]
print(lines)
count = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        count += 1
print(count)

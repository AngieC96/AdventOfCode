def get_input_int(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [int(line.strip()) for line in lines]
    return lines
def get_input_int(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [int(line.strip()) for line in lines]
    return lines

def get_input_str(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [str(line.strip()) for line in lines]
    return lines

def get_input_str_int(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.strip().split() for line in lines]
        lines = [(str(line[0]), int(line[1])) for line in lines]
    return lines
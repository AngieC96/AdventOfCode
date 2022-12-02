import os, sys

dir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_path, '..'))
from utilities.utility import get_input_str

#filename = os.path.join(dir_path, 'input_test.txt')
filename = os.path.join(dir_path, 'input.txt')
strategy_guide = get_input_str(filename)

my_score = {"X":1, "Y":2, "Z":3} # X for Rock, Y for Paper, and Z for Scissors
elf_score = {"A":1, "B":2, "C":3} # A for Rock, B for Paper, and C for Scissors
round_score = [[3, 6 , 0], [0, 3 ,6], [6, 0 ,3]]
score = 0
for round in strategy_guide:
    elf_move, my_move = round.split(" ")
    score += round_score[elf_score[elf_move]-1][my_score[my_move]-1] + my_score[my_move]

print(score)
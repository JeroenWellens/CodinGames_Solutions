import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
ladder = []

with open('source.txt') as f:

    w, h = [int(i) for i in f.readline().split()]
    for i in range(h):
        line = f.readline().split()
        ladder.append(line)

#make a dictionary of the top and bottom
ghost = {}
for i,j in zip(ladder[0],ladder[-1]):
    ghost.update({i:j})

#update the relations when going down the ladder
for step in ladder:
    if(len(step)<len(ladder[0])):
        moves = 0
        for i in range(len(step)):
            if('--' in step[i]):
                new_left = ladder[-1][i+moves+1]
                new_right = ladder[-1][i+moves]
                ghost.update({ladder[0][i+moves]:new_left})
                ghost.update({ladder[0][i+1+moves]:new_right})
                ladder[0][i+moves],ladder[0][i+1+moves]=ladder[0][i+1+moves],ladder[0][i+moves]
                moves += 1

for item in ghost:
    print(f'{item}{ghost[item]}')


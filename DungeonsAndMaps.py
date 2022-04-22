'''
4 4
1 1
3

0
.>>v
.^#v
..#v
...T

1
....
.v#.
.v#.
.>>T

2
....
v<#.
v.#.
..>T
'''


import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

with open('source.txt') as f:
    w, h = [int(i) for i in f.readline().split()]
    start_row, start_col = [int(i) for i in f.readline().split()]
    #number of maps
    n = int(f.readline())
    map_case = {}
    for i in range(n):
        maps = []
        for j in range(h):
            maps.append(f.readline())
        map_case.update({i:maps})
    
        
def next_tile(m,coord):
    x,y = coord
    if(m[y][x]=='<'):
        return (x-1,y)
    if(m[y][x]=='>'):
        return (x+1,y)
    if(m[y][x]=='^'):
        return (x,y-1)
    if(m[y][x]=='v'):
        return (x,y+1)
    
def route_length(grid,x,y):
    route = 0
    move = True
    coord = (x,y)
    start = (x,y)
    while(move):
        try:
            if(grid[coord[1]][coord[0]] == 'T'):
                move = False
                return route,True
            elif(start == coord and route != 0):
                return 0,False
            elif(grid[coord[1]][coord[0]] in '<>^v'):
                coord = next_tile(grid,coord)
                route += 1
            else:
                return route,False
        except:
            print('error')
            return route,False
        
    return 0,True
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
short = np.inf
use_map_number = 0
rich = False
for m in map_case:
    length,treasure = route_length(map_case[m],start_col,start_row)
    if(treasure):
        if(length < short):
            short = length
            use_map_number = m
            rich = treasure
        

if(rich):
    print(use_map_number)
else:
    print('TRAP')
#expected answer '1'
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mat = []
with open('source.txt') as f:
    for i in range(9):
        column = []
        for j in f.readline().split():
            column.append(int(j))
        mat.append(column)
matrix = np.array(mat)
print(matrix)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
solved = True
for r in range(9):
    confirmedr = []
    confirmedc = []
    confirmedg = []
    
    #check rows and columns
    for c in range(9):
        if matrix[r][c] in confirmedr:
            solved = False
            break
        else:
            confirmedr.append(matrix[r][c])
        if matrix[c][r] in confirmedc:
            solved = False
            break
        else:
            confirmedc.append(matrix[c][r])
    #check subgrid
    for d in range(9):
        if matrix[3*(r%3)+(d%3)][3*(r//3)+(d//3)] in confirmedg:
            solved = False
            break
        else:
            confirmedg.append(matrix[3*(r%3)+(d%3)][3*(r//3)+(d//3)])

if solved:
    print('true')
else:    
    print('false')

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

scrabble_points = {'e':1,'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,
                  'u':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,
                  'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}

# the dictionary of possibilities provided by the puzzle
oxford = []

with open('source.txt') as f:
    
    n = int(f.readline())
    for i in range(n):
        w = f.readline()
        # leaving out the '\n' at the end of the string of words
        oxford.append(w[:-1])
    # our tiles in the game
    options = list(f.readline())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
high_score = 0
solution = ''
# going through the words to see if we can use them.
for word in oxford:
    # make a copy of the options that we can manipulate
    letters = options.copy()
    score=0
    word_found = True
    # check if we can make the word
    for l in word:
        if l in letters:
            score += scrabble_points[l]
            # 'use' the letter
            letters.pop(letters.index(l))
        else:
            word_found=False
            break
    if word_found:
        if score > high_score:
            high_score = score
            solution = word
print(solution)




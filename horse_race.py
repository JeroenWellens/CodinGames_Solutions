import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

horse_strength = []

n = int(input())
for i in range(n):
    pi = int(input())
    horse_strength.append(pi)

horse_strength.sort()

last_strength = -1000
diff = []
for strength in horse_strength:
    diff.append(abs(strength - last_strength))
    last_strength = strength

diff.sort()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(diff[0])

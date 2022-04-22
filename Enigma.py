#case 1
#operation = 'ENCODE'
operation = 'DECODE'
pseudo_random_number = 4
rotor1 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotors = [rotor1,rotor2,rotor3]
#message = 'AAA'
message = 'KQF'


'''
#case 3
operation = 'DECODE'
pseudo_random_number = 9
rotor1 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotors = [rotor1,rotor2,rotor3]
message = 'PQSACVVTOISXFXCIAMQEM'
'''

import sys
import math

def ceasar_Shift(mes,num,encode):
    straight = {}
    for n in range(26):
        straight.update({alphabet[n]:n})
    code = ''
    count = 0
    if(encode):
        for l in mes:
            code += alphabet[(straight[l]+num+count)%26]
            count += 1
    else:
        for l in mes:
            code += alphabet[(straight[l]-num-count)%26]
            count += 1
    
    return code

def rotor_shift(mes,rotor):
    code = ''
    for l in mes:
        code += rotor[l]
    return code

#make dictionaries of the rotors

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d1 = {}
d2 = {}
d3 = {}

encode = operation == 'ENCODE'

for n in range(26):
    if(encode):
        d1.update({alphabet[n]:rotor1[n]})
        d2.update({alphabet[n]:rotor2[n]})
        d3.update({alphabet[n]:rotor3[n]})
    else:
        d1.update({rotor1[n]:alphabet[n]})
        d2.update({rotor2[n]:alphabet[n]})
        d3.update({rotor3[n]:alphabet[n]})
       
ds = {1:d1,2:d2,3:d3}

if(encode):
    cr1 = ceasar_Shift(message,pseudo_random_number,encode)
    r1 = rotor_shift(cr1,ds[1])
    r2 = rotor_shift(r1,ds[2])
    coded = rotor_shift(r2,ds[3])
else:
    d1 = rotor_shift(message,ds[3])
    d2 = rotor_shift(d1,ds[2])
    d3 = rotor_shift(d2,ds[1])
    coded = ceasar_Shift(d3,pseudo_random_number,encode)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(message)
print(coded)


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

inputs = {}
outputs_list = []
outputs_dict = {}
'''
Get the input data
'''
with open('source.txt') as f:
    
    n = int(f.readline()) # lines of input
    m = int(f.readline()) # lines of output
    for i in range(n):
        input_name, input_signal = f.readline().split()
        inputs.update({input_name: input_signal})
        input_length = len(inputs[input_name])

    for i in range(m):
        output_name, _type, input_name_1, input_name_2 = f.readline().split()
        outputs_list.append(output_name)
        outputs_dict.update({output_name: (_type, input_name_1, input_name_2)})

'''
do stuff
'''
################################################
###                                          ###
###    switching between text and boolean    ###  
###                                          ###
################################################


def decode(seg):
    '''
    Turn the input signal of underscore "_" into False
    and the input signal of minus "-" into True
    '''
    if seg=='_':
        return False
    if seg=='-':
        return True

def encode(seg):
    '''
    Turn the input False into an underscore "_"
    and the input True into a minus "-"
    '''
    if seg:
        return '-'
    else:
        return '_'

##############################
###                        ###
###    coding the gates    ###  
###                        ###
##############################

def gate_and(in1,in2):
    return (in1 and in2)

def gate_or(in1,in2):
    return (in1 or in2)

def gate_nand(in1,in2):
    return not(gate_and(in1,in2))

def gate_nor(in1,in2):
    return not(gate_or(in1,in2))

def gate_xor(in1,in2):
    if(in1 and in2):
        return False
    else:
        return (in1 or in2)

def gate_xnor(in1,in2):
    return not(gate_xor(in1,in2))

'''
get and give the answer
'''

for i in range(m):
    '''
    go through each of the tasks and get the solution.
    '''
    
    _type, input_name_1, input_name_2 = outputs_dict[outputs_list[i]]
    result = ''
    # print(f'input 1: ({input_name_1})')
    # print(inputs[input_name_1])
    # print(f'input 2: ({input_name_2})')
    # print(inputs[input_name_2])
    
    if _type == 'AND':
        for j in range(input_length): #go through the input 'letter' by 'letter'
            #transform string to boolean
            in1 = decode(inputs[input_name_1][j])
            in2 = decode(inputs[input_name_2][j])
            result += encode(gate_and(in1,in2))
    elif _type == 'OR':
        for j in range(input_length): #go through the input 'letter' by 'letter'
            #transform string to boolean
            in1 = decode(inputs[input_name_1][j])
            in2 = decode(inputs[input_name_2][j])
            result += encode(gate_or(in1,in2))
    elif _type == 'XOR':
        for j in range(input_length): #go through the input 'letter' by 'letter'
            #transform string to boolean
            in1 = decode(inputs[input_name_1][j])
            in2 = decode(inputs[input_name_2][j])
            result += encode(gate_xor(in1,in2))
    elif _type == 'NAND':
        for j in range(input_length): #go through the input 'letter' by 'letter'
            #transform string to boolean
            in1 = decode(inputs[input_name_1][j])
            in2 = decode(inputs[input_name_2][j])
            result += encode(gate_nand(in1,in2))
    elif _type == 'NOR':
        for j in range(input_length): #go through the input 'letter' by 'letter'
            #transform string to boolean
            in1 = decode(inputs[input_name_1][j])
            in2 = decode(inputs[input_name_2][j])
            result += encode(gate_nor(in1,in2))
    elif _type == 'NXOR':
        for j in range(input_length): #go through the input 'letter' by 'letter'
            #transform string to boolean
            in1 = decode(inputs[input_name_1][j])
            in2 = decode(inputs[input_name_2][j])
            result += encode(gate_xnor(in1,in2))
    else:
        result = _type
#    for j in range(length):
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(f'{outputs_list[i]} {result}')

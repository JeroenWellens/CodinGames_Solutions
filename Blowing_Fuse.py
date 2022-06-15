import sys
import math

'''
Input
Line 1: Integers n m c, separated by a space
n is the number of devices, assume the devices have IDs from 1 to n
m is the number of button-clicking going to happen
c is the capacity of the main fuse in amperes [A]

Line 2: n integers, space separated, representing the electrical current consumption value of each appliance, listed from ID 1 to n

Line 3: m integers, space separated - a sequence of ID# you are going to click power buttons, that will toggle the device status in that exact sequence.
'''

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
'''
Constraints
n and m are below 100
c is below 10000
'''

devices = {}
currents = [0]
maxcurrent = 0 
flips = []
fuse_blown = False

with open('source.txt') as f:

    n, m, c = [int(i) for i in f.readline().split()]
    
    #make a dictionary of devices with IDs from 1 to n
    
    for i in f.readline().split():
        nx = int(i)
        currents.append(nx)
 
    for i in f.readline().split():
        mx = int(i) #switch flips
        flips.append(mx)

for dev in range(1,n+1):
    devices.update({dev:(currents[dev],False)})    

def flip_switch(dev_id):
    '''
    updates the devices to reflect the flipped switch.
    
    args:
        dev_id: the id of the device to flip the switch
    '''
    devices.update({dev_id:(devices[dev_id][0],not devices[dev_id][1])})

def count_load():
    '''
    Goes through the devices and counts the acive load
    Retuns the load
    '''
    load = 0

    for dev in range(1,n+1):
        if devices[dev][1]:
            load += devices[dev][0]
    
    return load    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

'''
flip the switches one by one
'''

for flip_id in flips:
    flip_switch(flip_id)
    current_load = count_load()
    if current_load > maxcurrent:
        maxcurrent = current_load
    if maxcurrent> c:
        fuse_blown = True
        break
    
'''
Output
If the fuse was blown during the operation sequence, output one line:
Fuse was blown.

If the fuse did not blow, find the maximal consumed power by turned-on devices that occurred during the sequence. Output two lines:
Fuse was not blown.
Maximal consumed current was ? A.

Follow examples of test cases for the expected format.
'''




if fuse_blown:
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print(f"Maximal consumed current was {maxcurrent} A.")

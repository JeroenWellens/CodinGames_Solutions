import sys
import math

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

#interacting with station
connected = False

#location -1=idle,0=Diagnosis,1=Molecules,2=Laboratory
location = -1

###############################################
#   commands for what to do when connecting   #
###############################################
def movefrom(loc):
    switch = {
            -1 :todiagnosis(),
            0 : tomolecules(),
            1 : tolaboratory(),
            2 : todiagnosis()
        }

def diagnosis():
    pass

def molecules():
    pass
    
def laboratory():
    pass

def todiagnosis():
    connected = True
    print("GOTO DIAGNOSIS")

def tomolecules():
    connected = True
    print("GOTO MOLECULES")
    
def tolaboratory():
    connected = True
    print("GOTO LABORATORY")

# game loop
while True:
    for i in range(2):
        inputs = input().split()
        target = inputs[0]
        eta = int(inputs[1])
        score = int(inputs[2])
        storage_a = int(inputs[3])
        storage_b = int(inputs[4])
        storage_c = int(inputs[5])
        storage_d = int(inputs[6])
        storage_e = int(inputs[7])
        expertise_a = int(inputs[8])
        expertise_b = int(inputs[9])
        expertise_c = int(inputs[10])
        expertise_d = int(inputs[11])
        expertise_e = int(inputs[12])
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    sample_count = int(input())
    for i in range(sample_count):
        inputs = input().split()
        sample_id = int(inputs[0])
        carried_by = int(inputs[1])
        rank = int(inputs[2])
        expertise_gain = inputs[3]
        health = int(inputs[4])
        cost_a = int(inputs[5])
        cost_b = int(inputs[6])
        cost_c = int(inputs[7])
        cost_d = int(inputs[8])
        cost_e = int(inputs[9])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if not connected:
        movefrom(location)

    ####
    ##  commands to be printed:
    ####
    ##  "GOTO DIAGNOSIS"
    ##  "CONNECT id" where id[0,1,2]
    ##  "GOTO MOLECULES"
    ##  "CONNECT type" where type['A','B','C','D','E']
    ##  "GOTO LABORATORY"
    ##  "CONNECT id" where id[0,1,2]

    print("GOTO DIAGNOSIS")

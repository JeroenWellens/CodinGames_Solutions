
def do(lis):
    if(lis[0] == 'VALUE'):
        return int(lis[1])
    if(lis[0] == 'ADD'):
        return(int(lis[1])+int(lis[2]))
    if(lis[0] == 'SUB'):
        return(int(lis[1])-int(lis[2]))
    if(lis[0] == 'MULT'):
        return(int(lis[1])*int(lis[2]))

def operate(s,l):
    try:
        if('$' in s[l][1]):
            pos = int(s[l][1][1:])
            s[l][1] = operate(s,pos)
        if('$' in s[l][2]):
            pos = int(s[l][2][1:])
            s[l][2] =  operate(s,pos)
        return(do(s[l]))
    except:
        return(do(s[l]))    
    


with open('source.txt') as f:

    n = int(f.readline())
    sheet = {}
    for i in range(n):
        operation, arg_1, arg_2 = f.readline().split()
        sheet.update({i:[operation,arg_1,arg_2]})
    for line in sheet:
        print(operate(sheet,line))
        
        
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

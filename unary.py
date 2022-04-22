
message = '%'

#convert message to binary string
binary = ''.join(format(ord(i), '07b') for i in message)

#convert binary to blocks of 0

d = {'0':'00 ','1':'0 '}
previous = ''
count = 1
converted = ''

for letter in binary:
    if(letter == previous):
        count +=1
    else:
        if(previous == ''):
            previous = letter
            count = 1
        else:
            converted += d[previous] +'0'*count + ' '
            previous = letter
            count = 1
    
converted += d[previous] + '0'*count    

#C : 0 0 00 0000 0 00
#CC: 0 0 00 0000 0 000 00 0000 0 00
#% : 00 0 0 0 00 00 0 0 00 0 0 0
print(converted)

def pos(array2,letter):
    for i in range(5):
        for j in range(5):
            if array2[i][j]==letter:
                x=i
                y=j

    return x,y;

import string

key=raw_input('enter key please:  ')
key=''.join(e for e in key if e.isalpha())
array=[]

for e in key.upper():
    if e not in array:
        array.append(e)

alph="ABCDEFGHIKLMNOPQRSTUVWXYZ"

for e in alph:
    if e not in array:
        array.append(e)

array2=['' for e in range(5)]

for i in range(5):
    array2[i]=array[i*5:i*5+5]
    print '\n', array2[i]


mess=raw_input('Enter message:\n')
#REMOVE SPACES

message=[]

for e in mess:
    if e.isalpha():
        message.append(e)

#divide same letter pairs by adding X
for i in range(len(message)):
    if message[i]==message[i+1]:
        message.insert(i+1,'X')
    i=i+2
#add x if message has odd letters
if len(message)%2==1:
    message.append('X')

encrypt=['' for i in range(len(message))]
k=0

for i in range(len(message)/2):
    print message[i*2], message[i*2+1]


for i in range(len(message)/2):
    pos1x,pos1y=pos(array2,message[i*2])
    pos2x,pos2y=pos(array2,message[i*2+1])
    if pos1x==pos2x:
        #if rows are same, get the next letter in the row
        encrypt[i*2]=array2[pos1x][(pos1y+1)%5]
        encrypt[i*2+1]=array2[pos1x][(pos2y+1)%5]
    elif pos1y==pos2y:
        #if columns are same, get the next bottom letter in that column
        encrypt[i*2]=array2[(pos1x+1)%5][pos1y]
        encrypt[i*2+1]=array2[(pos2x+1)%5][pos2y]
    else:
        #if both rows and columns are diff, make a rectangle
        #and write the horizontal corner from given letter
        #example:   D E
        #           F G
        #if the message pair is GD, write FE

        encrypt[i*2]=array2[pos1x][pos2y]
        encrypt[i*2+1]=array2[pos2x][pos1y]



print ''.join(e for e in encrypt)


#now to decrypt

decrypt=['' for i in range(len(encrypt))]

for i in range(len(encrypt)/2):
    pos1x,pos1y=pos(array2,encrypt[i*2])
    pos2x,pos2y=pos(array2,encrypt[i*2+1])
    if pos1x==pos2x:
        decrypt[i*2]=array2[pos1x][(pos1y-1)%5]
        decrypt[i*2+1]=array2[pos1x][(pos2y-1)%5]
    elif pos1y==pos2y:
        decrypt[i*2]=array2[(pos1x-1)%5][pos1y]
        decrypt[i*2+1]=array2[(pos2x-1)%5][pos2y]
    else:
        decrypt[i*2]=array2[pos1x][pos2y]
        decrypt[i*2+1]=array2[pos2x][pos1y]

print ''.join(e for e in decrypt if e!='X')

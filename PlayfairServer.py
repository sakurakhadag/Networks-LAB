import string

def position(letter, array):
    for i in range(5):
        for j in range(5):
            if array[i][j]==letter:
                return i,j;





key=raw_input("Enter key please:  ")
key=key.upper()


alph="ABCDEFGHIKLMNOPQRSTUVWXYZ"

array=[]

for e in key:
  if e not in array:
    array.append(e)

for e in alph:
  if e not in array:
    array.append(e)

array2=[['' for i in range(5)] for j in range(5)]
print "Key array is"
for i in range(5):
  array2[i]=(array[i*5:i*5+5])
  print array2[i]


message=raw_input("Please enter message:   ")
message=message.upper()
message=''.join(e for e in message if e.isalpha())

for i in range(len(message)-1):
    if message[i]==message[i+1]:
        message=message[0:i+1]+'X'+message[i+1:]

if len(message)%2==1:
    message=message+'X'

for i in range(len(message)/2):
    print message[i*2],message[i*2+1]

#now we check positions of each letter in the key array

encrypted=['' for i in range(len(message))]

for i in range(len(message)/2):
    row1,col1=position(message[i*2],array2)
    row2,col2=position(message[i*2+1],array2)

    if row1==row2:
        encrypted[i*2]=array2[row1][(col1+1)%5]
        encrypted[i*2+1]=array2[row1][(col2+1)%5]
    elif col1==col2:
        encrypted[i*2]=array2[(row1+1)%5][col1]
        encrypted[i*2+1]=array2[(row2+1)%5][col1]
    else:
        encrypted[i*2]=array2[row1][col2]
        encrypted[i*2+1]=array2[row2][col1]

print "Encrypted message is: "
for i in range(len(encrypted)/2):
    print encrypted[i*2],encrypted[i*2+1],"  ",

print ''

import socket
port=12345
s=socket.socket()
s.bind(('',port))
s.listen(5)

while True:
    c,addr=s.accept()
    c.send(''.join(encrypted))
    c.close()
    break
s.close()

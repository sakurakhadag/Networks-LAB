import string

def position(letter, array):
    for i in range(5):
        for j in range(5):
            if array[i][j]==letter:
                return i,j;


import socket
port=12345
s=socket.socket()
s.connect(('127.0.0.1',port))
message=s.recv(1024)
print "Encrypted message is:",message

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

#now we check positions of each letter in the key array

encrypted=['' for i in range(len(message))]

for i in range(len(message)/2):
    row1,col1=position(message[i*2],array2)
    row2,col2=position(message[i*2+1],array2)

    if row1==row2:
        encrypted[i*2]=array2[row1][(col1-1)%5]
        encrypted[i*2+1]=array2[row1][(col2-1)%5]
    elif col1==col2:
        encrypted[i*2]=array2[(row1-1)%5][col1]
        encrypted[i*2+1]=array2[(row2-1)%5][col1]
    else:
        encrypted[i*2]=array2[row1][col2]
        encrypted[i*2+1]=array2[row2][col1]

if encrypted[-1]=='X':
    encrypted=encrypted[:-1]
decrypt=''
for i in range(len(encrypted)):
    if encrypted[i]=='X' and encrypted[i-1]==encrypted[i+1]:
        encrypted=encrypted[:i]+encrypted[i+1:]
print encrypted

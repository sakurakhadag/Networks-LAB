message=raw_input("Enter message")

#let number of rows be 3
while len(message)%3!=0:
    message+='X'

array=[['' for j in range(len(message)/3)] for i in range(3)]
encrypt=['' for i in range(len(message))]
counter=0
for j in range(len(message)/3):
    for i in range(3):
        array[i][j]=message[counter]
        counter+=1


for i in range(3):
    for j in range(len(message)/3):
        encrypt+=array[i][j]
encrypt= ''.join(encrypt)
print encrypt
#for decryption

array2=[['' for j in range(len(encrypt)/3)] for i in range(3)]
message=['' for i in range(len(encrypt))]
counter=0

for i in range(3):
    for j in range(len(encrypt)/3):
        array2[i][j]=encrypt[counter]
        counter+=1
print array2

decrypt=''
for j in range(len(encrypt)/3):
    for i in range(3):
        decrypt+=array2[i][j]
print ''.join(decrypt)

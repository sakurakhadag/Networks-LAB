import string

key=raw_input('Enter key please:    ')
#now remove all spaces from key
key = ''.join(e for e in key if e.isalpha())
print 'Given key is :',key

#initialise the 2X2 array for key
#yes I know my variable names suck
ka=[[0 for i in range(2)] for j in range(2)]
e=0

print 'The converted key matrix is:'

for i in range(2):
    for j in range(2):
        #convert each letter to its index and store in array
        #remember this function requires import string
        ka[i][j]=string.lowercase.index(key[e])
        e=e+1
    print ka[i][:]

#now ask for message
msg=raw_input('Please enter message:     ')
#remove extra characters
msg_wo_space=''.join(e for e in msg if e.isalpha())
print 'Entered message is ',msg

if(len(msg_wo_space)%2==1):
    msg.append('x')

#initialise encrypted message
encrypt=[]

#for each pair of letters in msg, convert to index and multiply to key array
k=0
i=0
for k in range(len(msg)/2):
    if(msg[i].isspace()):
        encrypt.append(' ')
        i=i+1
        x=string.lowercase.index(msg[i])
    else:
        x=string.lowercase.index(msg[i])
    if(msg[i+1].isspace()):
        i=i+1
        print 'Space found at i=',i+1
        flag=1
        y=string.lowercase.index(msg[i+1])

    else:
        flag=0
        y=string.lowercase.index(msg[i+1])

    for j in range(2):
        a=(ka[j][0]*x+ka[j][1]*y)%26
        encrypt.append(string.ascii_lowercase[a])

        if flag==1:
            flag=0
            encrypt.append(' ')

    i=i+2
print 'encrypted string is:'
print ''.join(e for e in encrypt)


# decryption now

#find multiplicative inverse of key array

d=ka[0][0]*ka[1][1]-ka[0][1]*ka[1][0]
d=d%26

for i in range(100):
    if (d*i)%26==1:
        break

d=i
#this is d inverse

#now we fing adjugate matrix of ka
#for 2X2 matrix [ a b ]
#               [ c d ]

#the adj(a) is [ d -b ]
#              [ -c a ]

temp=ka[0][0]
ka[0][0]=ka[1][1]
ka[1][1]=temp

ka[0][1]=-ka[0][1]
ka[1][0]=-ka[1][0]

#now we multiply this adj(matrix) with the multiplicative inverse we found
    #and then take mod by 26

for i in range(2):
    for j in range(2):
        ka[i][j]=(d*ka[i][j])%26

for i in range(2):
    print ka[i][:]

#now multipy pairs of encrypted message to inverse array
decrypt=[]

k=0
i=0

for k in range(len(encrypt)/2):
    flag=0
    if(encrypt[i].isspace()):
        decrypt.append(' ')
        i=i+1

    x=string.lowercase.index(encrypt[i])

    if(encrypt[i+1].isspace()):
        flag=1
        i=i+1

    y=string.lowercase.index(encrypt[i+1])

    for j in range(2):
        a=(ka[j][0]*x+ka[j][1]*y)%26
        decrypt.append(string.ascii_lowercase[a])
        if flag==1:
            decrypt.append(' ')
            flag=0
    i=i+2
print 'decrypted string is:'
print ''.join(e for e in decrypt)

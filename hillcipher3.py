import string

def adjoint(array):
    adj=[[0 for i in range(3)] for j in range(3)]

    for i in range(3):
        for j in range(3):

            a=array[(i+1)%3][(j+1)%3]*array[(i+2)%3][(j+2)%3]
            b=array[(i+2)%3][(j+1)%3]*array[(i+1)%3][(j+2)%3]

            #find cofactor for every element and then adding to adjoint matrix

            adj[j][i]=(a-b)%26

    #print 'Adjoint matrix is'
    #for i in range(3):
        #print adj[i][:]

    return adj;

key=raw_input('Enter key please:    ')
#now remove all spaces from key
key = ''.join(e for e in key if e.isalpha())
print 'Given key is :',key
array=[]

#initialise the 3X3 array for key
#yes I know my variable names suck
ka=[[0 for i in range(3)] for j in range(3)]
e=0

print 'The converted key matrix is:'
for e in range(len(key)):
    for i in range(i,3):
        for j in range(j,3):
            #convert each letter to its index and store in array
            #remember this function requires import string
            array.append(string.lowercase.index(key[e]))
k=0
if len(key)<9:
    for i in range(len(key),9):
            array.append(k)
            k=k+1

#print array

k=0
for i in range(3):
    for j in range(3):
            ka[i][j]=array[k]
            k=k+1
print ' Key Array is:'
for i in range(3):
    print ka[i][:]

#now ask for message
msg=raw_input('Please enter message:     ')
#remove extra characters
msg=''.join(e for e in msg if e.isalpha())

if len(msg)%3==1:
    msg+='xx'
elif len(msg)%3==2:
    msg+='x'
print 'Entered message is ',msg


#initialise encrypted message
encrypt=[]

#for each triplet of letters in msg, convert to index and multiply to key array
k=0
i=0
for k in range(len(msg)/3):
    x=string.lowercase.index(msg[i])
    y=string.lowercase.index(msg[i+1])
    z=string.lowercase.index(msg[i+2])

    for j in range(3):
        a=(ka[j][0]*x+ka[j][1]*y+ka[j][2]*z)%26
        encrypt.append(string.ascii_lowercase[a])

    i=i+3

print 'encrypted string is:'
print ''.join(e for e in encrypt)


# decryption now

kadj=[[0 for i in range(3)] for j in range(3)]

kadj=adjoint(ka)

#find determinant key array

d=ka[0][0]*kadj[0][0]+ka[0][1]*kadj[1][0]+ka[0][2]*kadj[2][0]
d=d%26

#now find (d`) such that d*d`=1mod26
#why do we do this?
for i in range(100):
    if (d*i)%26==1:
        break

d=i
#print 'd=',d

#now we multiply this adj(matrix) with the multiplicative inverse we found
    #and then take mod by 26

for i in range(3):
    for j in range(3):
        ka[i][j]=(d*kadj[i][j])%26

#print 'Inverse matrix is'
#for i in range(3):
    #print ka[i][:]

#now multipy pairs of encrypted message to inverse array
decrypt=[]

k=0
i=0

for k in range(len(encrypt)/3):
    x=string.lowercase.index(encrypt[i])
    y=string.lowercase.index(encrypt[i+1])
    z=string.lowercase.index(encrypt[i+2])

    for j in range(3):
        a=(ka[j][0]*x+ka[j][1]*y+ka[j][2]*z)%26
        decrypt.append(string.ascii_lowercase[a])

    i=i+3

print 'decrypted string is:'
print ''.join(e for e in decrypt)

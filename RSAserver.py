def exponentiate(x,y,p):
    res=1
    x=x%p
    while(y>0):
        if (y&1):
            res=(res*x)%p
        y=y>>1
        x=(x*x)%p
    return res;

n=int(raw_input("Enter modulus"))
d=int(raw_input("Enter private exponent"))

import socket
s=socket.socket()
port=12345
s.bind(('',port))
s.listen(5)
while True:
    c,addr=s.accept()
    data=c.recv(1024)
    data=int(data)
    print data
    c.close()
    break
s.close()

#decrypted message=(c^d)mod n
decrypt=exponentiate(data,d,n)
print decrypt
decrypt=str(decrypt)
if len(decrypt)%2==1:
    decrypt='0'+decrypt

message=[]

for i in range(len(decrypt)/2):
        no=int(decrypt[i*2:i*2+2])
        message.append(chr(no))

print message

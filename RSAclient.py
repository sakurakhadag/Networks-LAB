def isPrime(n):
    if n<=2 or n%2==0:
        return 0;
    elif all(n%i!=0 for i in range(3,int(n**0.5)+1,2)):
        return 1;
    else:
        return 0;

def isCoPrime(n,m):
    if n%m==0:
        return False;
    else:
        return True;

def Euclid(a,m):
    m0=m
    x=0
    y=1
    if m==1:
        return 0;
    while(a>1):
        q=a/m
        t=m
        m=a%m
        a=t
        t=x
        x=y-q*x
        y=t
    if y<0:
        y+=m0
    return y;

def exponentiate(x,y,p):
    #for (x^y)mod n
    result=1
    x=x%p

    while(y>0):
        if(y&1):
            result=(result*x)%p
        y=y>>1;
        x=(x*x)%p
    return result;

while True:
    P=int(raw_input("Enter the first prime number:  "))
    if isPrime(P):
        break
    print "Number is not prime"

while True:
    Q=int(raw_input("Enter the second prime number:  "))
    if isPrime(Q):
        break
    print "Number is not prime"

n=P*Q
totient=(P-1)*(Q-1)

while True:
    ex=int(raw_input("Enter exponent of public key:  "))
    if isCoPrime(ex,totient):
        break
    print "The number is invalid"

d=Euclid(ex,totient)
print d

print "Public key is ",n,", ",ex
#private key is n,d

import string

message=raw_input("Enter message:  ")
msg=''
for e in message:
    if e.isalpha() or e.isspace() or e.isdigit():
            msg+=e
message=''.join(msg)

message=message.upper()

#now convert to ASCII
c=[]
for i in message:
    c.append(str(ord(i)-65))
#make sure all numbers are 2 digit
for i in range(len(c)):
    if len(c[i])==1:
        c[i]='0'+c[i]

c=int(''.join(map(str,c)))
#print c

encrypt=exponentiate(c,ex,n)
print encrypt

import socket
s=socket.socket()
port=12345
s.connect(('127.0.0.1',port))
s.send(str(encrypt))
s.close()

port =12345
import socket
import string

plainText=raw_input("Enter message\t:")
plainText=plainText.lower()
plainText=''.join(e for e in plainText if e.isalpha())
encrypted=['' for i in range(len(plainText))]
for i in range(len(plainText)):
    encrypted[i]=(string.lowercase.index(plainText[i])+3)%26
    encrypted[i]=chr(encrypted[i]+97)
print "Encrypted message is: ",''.join(encrypted)

s=socket.socket()
s.bind(('',port))
s.listen(5)
while True:
    c,addr=s.accept()
    #print "Socket is connected to", addr
    c.send(''.join(encrypted))
    print c.recv(1024).decode()
    c.close()
    break
s.close()

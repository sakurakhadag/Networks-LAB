port=12345
import socket
import string
s=socket.socket()
s.connect(('127.0.0.1',port))
encrypted=s.recv(1024)
print "Encrypted text is",encrypted
message=[]
for i in range(len(encrypted)):
    message.append((string.lowercase.index(encrypted[i])-3)%26)
    message[i]=chr(message[i]+97)
print "Decrypted message is: ",''.join(message)
print len(message)

s.send("Bye")
s.close()

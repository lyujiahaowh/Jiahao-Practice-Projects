'''
Network programs - Part 3
ASCII == American Standard Code for Information Interchange
Basically, one number equal one letter, which means computer store them as numbers

Representing Simple Strings 
- Each character is represented by a number between 0 and 256 stored in 8 bits of memory
- We offer to "8 bits of memory as a "byte" of memory -(i.e. my disk drive contains 3 Terabytes of memory)"
- The ord() function tells us the numeric value of a simple ASCII cahracter
- In the 1960s and 1970s, we just assumed that one byte was one character

Unicode == universal code

Multi-Byte Characters
- To represent the wide range of characters computers must handle we represent characters with more than one byte
-- UTF-16 - Fixed length - Two bytes
-- UTF-32 - Fixed length - Four bytes
-- UTF-8 - 1-4 bytes
--- Upwards compatible with ASCII
--- Automatic detection between ASCII and UTF-8
--- UTF-8 is recommended practice for encoding data to be exchanged between systems
p.s. 
In Python2 byte string and regular string are same, the Unicode string are the different. 
In Python3 byte string and regular string are different but Unicode string are the same.
So bytes turns out to be raw, unencoded, that might be UTF-8, might be UTF-16, it might be ASCII

Python3 and Unicode
- In Python3, all strings internally are UNICODE
- Working with string variables in Python programs and reading data from files usually "just works"
- When we talk to a network resource using sockets or talk to a database we have to encode and decode data(Usually to UTF-8)

Python Strings to Bytes
- When we talk to an external resource like a network socket we sends bytes, so we need to encode Python3 strings into a given character encoding
- When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python3 as a string
e.g.
while True:
    data = mysock.recv(512)
    if ( lem(data) < 1 ) :
        break
    mystring = data.decode()
    print(mystring)
- 'data' here is Bytes string and 'mystring' is Unicode string, 'decode()' is UTF-8 on ASCII

An HTTP Request in Python
// this is an example code
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() // this the Bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

'''


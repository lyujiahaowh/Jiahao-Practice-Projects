'''
Application Protocol
- Since TCP(and Python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
- Application Portocols
 - Mail
 - World Wide Web

HTTP - Hypertext Transfer Protocol
- The dominant Application Layer Protocol on the Internet
- Invented for the Web - to Retrieve HTML, Images, Documents, etc
- Extended to be data in addition to documents - RSS, Web Services, etc.. Basic Concept - Make a Connection - Request a document
- Rectrieve the Document - Close the Connection
- HTTP is the set of rules to allow browsers to retrieve web documents from servers over the Internet

What is a Protocol?
- A set of rules that all parties follow so we can predict each other''s behavior
- And not bump into each other
 - On two-way roads in USA, drive on the right-hand side of the road
 - On two-way roads in the UK, drive on the left-hand side of the road

example : http://www.dr-chuck.com/page1.htm
"http" is the protocol, "www.dr-chuck.com" is the host, "page1.htm" is the document

Getting Data From the Server
- Each the user clicks on an anchor tag with an href= value to switch to a new page,
the browser makes a conncetion to the web server and issues a "GET" request - to GET the content of the page at the specified URL
- THe server returns the HTML document to the Browser which formats and displays the doucment to the user.

Internet Standards
- THe standards for all of the Internet protocol(inner workings) are developed by an organization
- Internet Engineering Taks Force (IETF)
- www.ietf.org
- Standards are called "RFCs" - "Request for Comments"

Making an HTTP request
- Connects to the server like www.dr-chuck.com
- Request a document (or the default document)
 - GET http://www.dr-chuck.com/page1.htm HTTP/1.0
 - GET http://www.mlive.com/ann-arbor/ HTTP/1.0
 - GET http://www.facebook.com HTTP/1.0

Web Server <-> Browser

$ telnet www.dr-chuck.com 80
Trying 74.208.28.177...
Connected to www.dr-chuck.com.Escape character is '^]'.
GET http://www.dr-chuck.com/page1.htm HTTP/1.0

// Metadata = HTTP Header 
HTTP/1.1 200 OK
Date: Thu, 08 Jan 2015 01:57:52 GMT
Last-Modified: Sun, 19 Jan 2014 14:25:43 GMT
Connection: close
Content-Type: text/html

// Content of file
<h1>The First Page</h1>
<p>If you like, you can switch to 
the <a href="http://www.dr-chuck.com/page2.htm">Second Page</a>.</p>
Connection closed by foreign host.


An HTTP Request in Python 
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()

'''
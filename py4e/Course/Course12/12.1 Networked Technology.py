'''
Transport Control Protocol(TCP)
- Built on the top of IP(Internet Protocol)
- Assumes IP might lose some data - stores and restransmits data if it seems to be lost
- Handles "flow control" using a transmit window
- Provides a nice reliable pipe

TCP connections/ Socks
"In computer networking, an Internet socket or network socket is an endpoint of a bidirectional inter-process communication flow
across an Internet Protocol-based computer network, such as the Internet."

Sockets in Pythons
Python has built-in support for TCP Sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) // in here, data.pr4e.org is the Host, 80 is the Port

Common TCP Ports : http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers 
- Telnet (23) - Login
- SSH (22) - Secure Login
- HTTP (80)
- HTTPS (443) - Secure
- SMTP (25) (Mail)
- IMAP (143/220/993) - Mail Retrieval
- POP (109/110) - Mail Retrieval
- DNS (53) - Domain Name
- FTP (21) - File Transfer
'''
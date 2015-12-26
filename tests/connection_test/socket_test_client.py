import socket
from sys import argv

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', int (argv [1])))

while True:    
    
    
    send_content = raw_input('Text: ')
    s.send (send_content)
    
    data = s.recv (1024)
    
    if data:
        print data
    elif data == 'stop':
        break
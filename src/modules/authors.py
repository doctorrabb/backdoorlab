from colorama import Fore, init
import webbrowser
import datetime

init ()


banner = '''

###################################
#         BLACK HAT LTD.          #
#   Vladislav Kotov (DOCTOR_RABB) #
###################################

'''

def print_authors ():
    print Fore.CYAN + banner + Fore.RESET
    
def print_prz_banner ():
    dt = str (datetime.date.today ()).split ('-')
    if dt[1] == '01' or dt[1] == '12':
        ylk = '''
    _______*__________
    ______*0*_________
    _____*0*0*________
    ____*0*0*0*_______
    ___*0*0*0*0*______
    ___0*0*0*0*0*_____
    _____|| ||________
       Happy New Year :)
        '''
        print Fore.WHITE + ylk + Fore.RESET
    elif dt[1] == '01' and dt[2] == '31':
        print Fore.YELLOW + '*'*60
        print ' '*10 + Fore.WHITE + 'Today is DOCTOR_RABBs birthday!' + ' '*10
        print Fore.YELLOW + '*'*60 + Fore.RESET
        print ''
        if raw_input ('Do you want to congratulate him? (y/n): ') == 'y':
            webbrowser.open ('https://www.facebook.com/profile.php?id=100010748175794')


#!/usr/bin/env python

#importing modules
import stdiomask as sm
import os
from colored import fg, bg, attr

#defining the terms
red = fg(1) + bg(232)
red2 = fg(1)
green = fg(2) + bg(232)
green2 = fg(2)
blue = fg(57) + bg(232)
blue2 = fg(57)
reset = attr("reset")

#the main program
def main_menu():
    print ( red + "Choose any 1 choice" + reset )
    print ( red + "1.Register new lock" + reset + "\n" + red + "2.Exit" + reset ) 
def register():
    usr = input( blue + 'Enter username : ' + reset + blue2 )  
    pw = input( green  + 'Enter password : ' + reset + green2 )
    rpw = sm.getpass( green + 'Retype password : ' + reset + green2,mask='*' )
    if pw == rpw:
        if len(pw) >= 6 :
            os.system("touch .usr_pass")
            uspswd = open(".usr_pass",'w')
            uspswd.writelines(usr+'\n')
            uspswd.writelines(pw+'\n')
            print ( green + 'lock sucessfully registered' + reset )
            os.system ("bash file/setup.sh ")
            exit()
        else :
            print( red + "Password must be atkeast 6 digit long" + reset )
            register()
    else:
        print ( red + "Password Did Not Match" + reset )
        register()
def check_usr_pass():
    while True:
        try:
            try:
                user = input( blue + "Enter username : " + reset + blue2)
                pwd = sm.getpass( green + "Enter password : " + reset + green2,mask="*")
                break
            except ValueError:
                print ( red + "wrong input" + reset )
        except KeyboardInterrupt:
            print ( red + "wrong input" + reset )
    uspass = open(".usr_pass",'r')
    lines = uspass.readlines()
    uspass.close
    if (len(lines) >= 2):
        usr = lines[0]
        paswd = lines[1]
        if user+'\n' == usr and pwd+'\n' == paswd:
            print ( green + "sucess" + reset )
            print ( green + "[★] Welcome to the termux [★]" + reset )
            exit()
        else:
            print ( red + "Invalid Credentials" + reset )
        check_usr_pass()
    else:
        print ( blue + "You Have Removed You Password" + reset )
        main_menu()
        final()
def final():
    menu = {1:register,2:exit}
    while True:
        try:
            choice = int(input( green + "Your Choice : " + reset ))
            break
        except ValueError:
            print ( red + "Wrong Input" + reset )
    if choice < 3 :
        menu[choice]()
    else:
        print ( red + 'Wrong Input' + reset )
        final()

print( green2 +  '''
━┏┛  ┃  ┏━┃┏━┛┃ ┃
 ┃ ━┛┃  ┃ ┃┃  ┏┛  
 ┛   ━━┛━━┛━━┛┛ ┛
 ''' + reset )
if __name__ == '__main__':
    check_usr_pass()

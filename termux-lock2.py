#!/usr/bin/env python

#modules
import os
from time import sleep
import stdiomask as sm
from colored import fg, bg, attr

#terms and colours
red = fg(1) + bg (232)
red2 = fg(1)
green = fg(2) + bg (232)
green2 = fg(2)
blue = fg(57) + bg(232)
blue2 = fg(57)
reset = attr("reset")

def main_menu():
    print ( fg(118) + bg(232) + "Choose The Option From Below." + reset )
    print ( green + "1.Register lock" + reset + "\n" + red  + "2.REMOVE LOCK" + reset + "\n" + blue + "3.EXIT" + reset )
def register():
    usr = input( blue + 'Enter username : ' + reset + blue2)
    pw = input( green + 'Enter password : ' + reset + green2)
    rpw = sm.getpass( red + 'Retype password : ' + reset + red2 ,mask='*')
    if pw == rpw:
        if len(pw) >= 6 :
            os.system("touch .usr_pass")
            uspswd = open(".usr_pass",'w')
            uspswd.writelines(usr+'\n')
            uspswd.writelines(pw+'\n')
            print ( green + 'lock sucessfully registered' + reset )
            os.system("bash $PREFIX/share/T-lock/files/setup.sh")
            exit()
        else :
            print ( red + "Password must be atkeast 6 digit long" + reset )
            register()
    else:
        print ( red + "Password Did Not Match" + reset )
        register()
def remove_pass():
    while True:
        try:
            try:
                user = input( blue + "Enter username : " + reset + blue2 )  
                pwd = sm.getpass( green + "Enter password : " + reset + green2,mask="*")
                break
            except ValueError:
                print ( red + "wrong input" + reset )
        except KeyboardInterrupt:
            print ( red + "wrong inout" + reset )
    uspass = open(".usr_pass",'r')
    lines = uspass.readlines()
    uspass.close
    usr = lines[0]
    paswd = lines[1]
    if user+'\n' == usr and pwd+'\n' == paswd:
        print ( blue + "Removing Your Lock" + reset )
        if(len(lines) >= 2):
            w = open(".usr_pass",'w')
            w.writelines([item for item in lines[:-2]])
            w.close()
        else:
            print ( red + 'have already removed your lock' + reset )
            exit()
        sleep(1)
        print ( green + "Lock successfully removed" + reset )
        os.system("bash $PREFIX/share/T-lock/files/origial/back.sh")
    else:
        print ( red + "Exited due to invalid credentials" + reset )
        print ( red2 + "Lock did not removed" + reset ) 
        exit()
def final():
    menu = {1:register,2:remove_pass,3:exit}
    while True:
        try:
            choice = int(input( green + "Your Choice : " + reset + green2 ))
            break
        except ValueError:
            print ( red + "Wrong Input" + reset )
    if choice <= 3 :
        menu[choice]()
    else:
        print ( red + 'Wrong Input' + reset )
        final()
if __name__ == '__main__':
    print ( fg(82) + '''
    ━┏┛  ┃  ┏━┃┏━┛┃ ┃
     ┃ ━┛┃  ┃ ┃┃  ┏┛ 
     ┛   ━━┛━━┛━━┛┛ ┛
    ''' + reset )
    main_menu()
    final()

#/usr/bin/bash

echo -e "removing the lock from login page of the terminal" | lolcat -p -F -f
rm -rf $PREFIX/etc/bash.bashrc
sleep(2)
cp bash.bashrc $PREFIX/etc
cp motd $PREFIX/etc
rm $PREFIX/bin/remove-pass
rm -rf $PREFIX/share/T-lock
sleep(2)
clear
figlet T-LOCK | lolcat -p -F -f
echo -e "OPEN NEW TERMINAL TO SEE CHANGES" | lolcat -p -f -F


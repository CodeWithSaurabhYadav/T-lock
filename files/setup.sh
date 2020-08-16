#/usr/bin/bash

echo -e "figlet setting up the lock to the login page of the terminal" | lolcat -p -F -f
rm -rf $PREFIX/etc/bash.bashrc
rm -rf $PREFIX/etc/motd
sleep 2.0
cp bash.bashrc $PREFIX/etc
mv ../../T-lock $PREFIX/share
cp remove-pwd $PREFIX/bin
chmod 777 $PREFIX/bn/remove-pass
sleep 2.0
clear
figlet T-LOCK | lolcat -p -F -f
echo -e "OPEN NEW TERMINAL TO SEE CHANGES" | lolcat -p -f -F

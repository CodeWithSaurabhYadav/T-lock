if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi
clear
figlet T-LOCK | lolcat
python3 $PREFIX/share/T-lock/termux-lock.py
PS1='\$ '

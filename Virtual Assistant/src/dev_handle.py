import os
def restart():
	os.system('reboot')
def shut_down():
	os.system("shutdown now -h")
def lock_device():
	os.popen('gnome-screensaver-command --lock')
	return 0

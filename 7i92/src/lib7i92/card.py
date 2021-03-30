import os, sys, subprocess
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def get_ip(parent):
	if parent.ipAddressCB.currentText() == 'Custom':
		return parent.customipLE.text()
	else:
		return parent.ipAddressCB.currentText()

def check_emc():
	if "0x48414c32" in subprocess.getoutput('ipcs'):
		return True
	else:
		return False

def readCard(parent, card):
	if check_emc():
		parent.errorMsgOk(f'LinuxCNC must NOT be running\n to read the {card}', 'Error')
		return
	ipAddress = get_ip(parent)
	arguments = ["--device", card, "--addr", ipAddress, "--readhmid"]
	parent.extcmd.job(cmd="mesaflash", args=arguments, dest=parent.flashPTE)

def flashCard(parent, card):
	if check_emc():
		parent.errorMsgOk(f'LinuxCNC must NOT be running\n to flash the {card}', 'Error')
		return
	ipAddress = get_ip(parent)
	if parent.firmwareCB.currentData():
		parent.statusbar.showMessage(f'Flashing the {card}...')
		ipAddress = parent.ipAddressCB.currentText()
		firmware = os.path.join(parent.lib_path, parent.firmwareCB.currentData())
		arguments = ["--device", card, "--addr", ipAddress, "--write", firmware]
		parent.extcmd.job(cmd="mesaflash", args=arguments, dest=parent.flashPTE)
	else:
		parent.errorMsgOk('A firmware must be selected', 'Error!')

def reloadCard(parent, card):
	if check_emc():
		parent.errorMsgOk(f'LinuxCNC must NOT be running\n to reload the {card}', 'Error')
		return
	ipAddress = get_ip(parent)
	arguments = ["--device", card, "--addr", ipAddress, "--reload"]
	parent.extcmd.job(cmd="mesaflash", args=arguments, dest=parent.flashPTE)

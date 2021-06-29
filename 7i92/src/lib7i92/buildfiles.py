import os, subprocess
from datetime import datetime

def build(parent):
	parent.tabs.setCurrentIndex(0)
	parent.machinePTE.clear()
	backup(parent)
	builddirs(parent)
	buildini(parent)
	buildhal(parent)
	buildio(parent)
	buildmisc(parent)

def backup(parent):
	if parent.backupCB.isChecked():
		if os.path.exists(parent.configPath): # there is something to backup
			backupDir = os.path.join(parent.configPath, 'backups')
			if not os.path.exists(backupDir):
				os.mkdir(backupDir)
			backupFile = os.path.join(backupDir, f'{datetime.now():%m-%d-%y-%H:%M:%S}')
			parent.machinePTE.appendPlainText(f'Backing up Files to {backupFile}')
			p1 = subprocess.Popen(['find',parent.configPath,'-maxdepth','1','-type','f','-print'], stdout=subprocess.PIPE)
			p2 = subprocess.Popen(['zip','-j',backupFile,'-@'], stdin=p1.stdout, stdout=subprocess.PIPE)
			p1.stdout.close()
			output = p2.communicate()[0]
			parent.machinePTE.appendPlainText(output.decode())

def builddirs(parent):
	if not os.path.exists(os.path.expanduser('~/linuxcnc')):
		os.mkdir(os.path.expanduser('~/linuxcnc'))
		parent.machinePTE.appendPlainText('Building LinuxCNC Directories')
	if not os.path.exists(os.path.expanduser('~/linuxcnc/configs')):
		os.mkdir(os.path.expanduser('~/linuxcnc/configs'))
	if not os.path.exists(os.path.expanduser('~/linuxcnc/nc_files')):
		os.mkdir(os.path.expanduser('~/linuxcnc/nc_files'))
	if not os.path.exists(os.path.expanduser('~/linuxcnc/subroutines')):
		os.mkdir(os.path.expanduser('~/linuxcnc/subroutines'))

def buildini(parent):
	iniFile = os.path.join(parent.configPath, parent.configName + '.ini') 
	parent.machinePTE.appendPlainText(f'Building the ini file: {iniFile}')

def buildhal(parent):
	halFile = os.path.join(parent.configPath, parent.configName + '.hal') 
	parent.machinePTE.appendPlainText(f'Building the hal file: {halFile}')

def buildio(parent):
	ioFile = os.path.join(parent.configPath, parent.configName + '.ini') 
	parent.machinePTE.appendPlainText(f'Building the io file: {ioFile}')

def buildmisc(parent):
	# if Axis is the GUI add the shutup file
	print(parent.guiCB.currentData())
	if parent.guiCB.currentData() == 'axis':
		shutupFilepath = os.path.expanduser('~/.axisrc')
		shutupContents = ['root_window.tk.call("wm","protocol",".","WM_DELETE_WINDOW","destroy .")']
		try: # if this file exists don't write over it
			with open(shutupFilepath, 'x') as shutupFile:
				shutupFile.writelines(shutupContents)
			parent.machinePTE.appendPlainText(f'Building the .axisrc file: {shutupFilepath}')
		except FileExistsError:
			pass
		except OSError:
			parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')

	#iniFile = os.path.join(parent.configPath, parent.configName + '.ini') 
	#parent.machinePTE.appendPlainText(f'Building the ini file: {iniFile}')

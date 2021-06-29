import configparser, os

def openFile(parent, ini):
	config = configparser.ConfigParser(strict=False)
	parent.machinePTE.clear()
	if config.read(ini):
		if config.has_option('7I92', 'VERSION'):
			iniVersion = config['7I92']['VERSION']
			if not iniVersion == parent.version:
				msg = ('The ini file version is {iniVersion}\n'
				'The Configuration Tool version is {self.version}\n'
				'Try and open the ini?')
				if not parent.errorMsgOkCancel(msg, 'Version Difference'):
					return False
		else:
			msg = ('This ini file has been built with an different version\n'
			'of this Configuration Tool\n'
			'Try and open?')
			if not parent.errorMsgOkCancel(msg, 'No Version'):
				return False
		parent.open_gui = True
		parent.nameLE.setText(os.path.splitext(os.path.basename(ini))[0])
		parent.pathOkLbl.setText('Config Opened')
		parent.open_gui = False
		#print(os.path.splitext(os.path.basename(ini))[0])

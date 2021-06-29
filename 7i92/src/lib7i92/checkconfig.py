def check(parent):
	configError = False
	tabError = False
	parent.tabs.setCurrentIndex(0)
	parent.machinePTE.clear()
	parent.machinePTE.insertPlainText('Checking Configuration for Errors\n')


	# check the Machine Tab for errors
	machineErrors = []
	if not parent.nameLE.text():
		tabError = True
		configError = True
		machineErrors.append('\tA configuration name must be entered')

	if tabError:
		machineErrors.insert(0, 'Machine Tab:')
		parent.machinePTE.insertPlainText('\n'.join(machineErrors))
		tabError = False
	# end of Machine Tab

	if not configError:
		parent.machinePTE.insertPlainText('No Errors found in Configuration')

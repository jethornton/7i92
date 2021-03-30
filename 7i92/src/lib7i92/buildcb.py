def build(parent):
	build_firmware(parent)

def build_firmware(parent):
	firmwareList = [
	['Select', False],
['7i92_5ABOB_Enc', '7i92_5ABOB_Enc.bit'],
['7i92_5ABOBx2D', '7i92_5ABOBx2D.bit'],
['7i92_7i76_7i74D', '7i92_7i76_7i74D.bit'],
['7i92_7i76_7i74d6ss', '7i92_7i76_7i74d6ss.bit'],
['7i92_7i76_7i78D', '7i92_7i76_7i78D.bit'],
['7i92_7i76x1D', '7i92_7i76x1D.bit'],
['7i92_7i76x1dpl', '7i92_7i76x1dpl.bit'],
['7i92_7i76x2d_2pwm', '7i92_7i76x2d_2pwm.bit'],
['7i92_7i76x2D', '7i92_7i76x2D.bit'],
['7i92_7i77_7i74D', '7i92_7i77_7i74D.bit'],
['7i92_7i77_7i76D', '7i92_7i77_7i76D.bit'],
['7i92_7i77_7i78d', '7i92_7i77_7i78d.bit'],
['7i92_7i77_7i85d', '7i92_7i77_7i85d.bit'],
['7i92_7i77_7i85sd', '7i92_7i77_7i85sd.bit'],
['7i92_7i77x2', '7i92_7i77x2.bit'],
['7i92_7i77x2D', '7i92_7i77x2D.bit'],
['7i92_7i78x2D', '7i92_7i78x2D.bit'],
['7i92_7i85sx2D', '7i92_7i85sx2D.bit'],
['7i92_7i85x2D', '7i92_7i85x2D.bit'],
['7i92_7i88ssx1', '7i92_7i88ssx1.bit'],
['7i92_BENEZANx2D', '7i92_BENEZANx2D.bit'],
['7i92_C11Gx2', '7i92_C11Gx2.bit'],
['7i92_C11Gx2D', '7i92_C11Gx2D.bit'],
['7i92_C11x2D', '7i92_C11x2D.bit'],
['7i92_DMMBOB1x2D', '7i92_DMMBOB1x2D.bit'],
['7i92_fallback', '7i92_fallback.bit'],
['7i92_g540_7i85sd', '7i92_g540_7i85sd.bit'],
['7i92_g540_85sd', '7i92_g540_85sd.bit'],
['7i92_G540x2D', '7i92_G540x2D.bit'],
['7i92_HDBB2Dx2', '7i92_HDBB2Dx2.bit'],
['7i92_MX3660x2D', '7i92_MX3660x2D.bit'],
['7i92_MX4660x2D', '7i92_MX4660x2D.bit'],
['7i92_PMDX126x2D', '7i92_PMDX126x2D.bit'],
['7i92_PROB_RFx2D', '7i92_PROB_RFx2D.bit'],
['7i92_R990x2D', '7i92_R990x2D.bit']
]

	for item in firmwareList:
		parent.firmwareCB.addItem(item[0], item[1])

	parent.unitsCB.addItem('Imperal', 'inch')
	parent.unitsCB.addItem('Metric', 'mm')

	parent.ipAddressCB.addItem('10.10.10.10')
	parent.ipAddressCB.addItem('192.168.1.121')
	parent.ipAddressCB.addItem('Custom')

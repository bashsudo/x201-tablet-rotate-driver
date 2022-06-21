import time, subprocess, getopt, sys

# 2020 Eiza Stanford
# ThinkPad X201 Tablet Display: Rotation and Calibration

class driver:

	def shellExecute(self, command):
		shellCommandOutput = str(subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1])

		return shellCommandOutput


	def shellOutputFilterBlanket(self, string, targets):
		for target in targets:
			stringSplit = string.split(target)

			for i in range(stringSplit.count('')):
				stringSplit.remove('')

			string = target.join(stringSplit)

		return string


	def tabletSensorInfoGet(self, tabletSensor, sensorAttribute):
		return self.tabletSensorDatabase[tabletSensor][sensorAttribute]


	def tabletSensorOrientationGet(self, tabletSensor):
		return str(self.shellExecute(['xsetwacom', '--get', self.tabletSensorInfoGet(tabletSensor, 'id'), 'Rotate']))


	def tabletDisplayRotate(self, direction):
		tabletOrientationString = self.tabletSensorOrientationGet(self.tabletModelSensor)
		print(tabletOrientationString)
		tabletOrientationNum = self.orientationNumDict[tabletOrientationString]
		tabletOrientationNum += direction

		if tabletOrientationNum > 3:
			tabletOrientationNum = 0
		elif tabletOrientationNum < 0:
			tabletOrientationNum = 3

		print('tabletDisplayRotate: xrandr orientation number is now %d' % tabletOrientationNum)

		self.shellExecute(['xrandr', '-o', str(tabletOrientationNum)])
		print('tabletDisplayRotate: rotated tablet display in direction \'%s\'' % (direction))


	def tabletSensorOrientationSync(self):
		tabletOrientation = self.shellExecute(['xsetwacom', '--get', self.tabletModelID, 'Rotate'])
		print('tabletSensorOrientationSync: model sensor is \'%s\' - orientation is \'%s\'' % (self.tabletModelSensor, tabletOrientation))

		for sensor in self.tabletSensorNames:
			if not sensor == self.tabletModelSensor:
				self.shellExecute(['xsetwacom', '--set', self.tabletSensorInfoGet(sensor, 'id'), 'Rotate', tabletOrientation])


	def tabletSensorReadjust(self):
		for sensor in self.tabletSensorNames:
			self.shellExecute(['xsetwacom', '--set', self.tabletSensorInfoGet(sensor, 'id'), 'ResetArea'])


	def driverParameters(self):
		wordList = sys.argv

		if len(wordList)<= 1:
			return

		argumentList = wordList[1:]

		optionsUnix = 'd:'
		optionsGNU = ['direction=']

		try:
			argumentListProc, valueListProc = getopt.getopt(argumentList, optionsUnix, optionsGNU)

		except getopt.error as error:
			print(str(error))
			sys.exit(2)

		for argument, value in argumentListProc:
			if argument in ('-d', '--direction'):
				self.tabletDisplayRotateDirection = int(value)
				print('OPTION: direction = \'%s\'' % (value))


	def tabletInfoGenerate(self):
		print('tabletInfoGenerate:')

		shellOutput = self.shellExecute(['xsetwacom', '--list', 'devices'])
		self.tabletSensorDatabase = {}

		if not shellOutput == '':
			shellOutputLines = shellOutput.split('\n')

			for line in shellOutputLines:
				lineFiltered = self.shellOutputFilterBlanket(line, [' '])

				splitTab = lineFiltered.split('\t')
				splitTabSpaceLeft = splitTab[0].split(' ')
				splitTabSpaceRight = splitTab[1].split(' ')

				tabletDevice = ' '.join(splitTabSpaceLeft[:-1])
				tabletSensor = str(splitTabSpaceLeft[-1:][0])
				tabletSensorID = str(splitTabSpaceRight[1])

				self.tabletSensorDatabase[tabletSensor] = {}

				tabletSensorInfo = self.tabletSensorDatabase[tabletSensor]
				tabletSensorInfo['device'] = tabletDevice
				tabletSensorInfo['id'] = tabletSensorID

				print('\tSENSOR \'%s\' | ID \'%s\' | DEVICE \'%s\'' % (tabletSensor, tabletSensorID, tabletDevice)) 

		self.tabletSensorNames = list(self.tabletSensorDatabase.keys())


	def __init__(self):
		# >>> Defining misc global variables
		self.tabletDisplayRotateDirection = 1
		self.orientationNumDict = {'none':0, 'ccw':1, 'half':2, 'cw':3}

		# >>> Retrieving program options from execution in shell
		self.driverParameters()

		# >>> Building tablet sensor information database
		self.tabletInfoGenerate()

		# >>> Defining global variables for the model tablet sensor & ID
		self.tabletModelSensor = 'stylus'
		self.tabletModelID = self.tabletSensorInfoGet(self.tabletModelSensor, 'id')

		# >>> Rotating tablet display in given direction
		self.tabletDisplayRotate(self.tabletDisplayRotateDirection)

		# >>> Waiting
		time.sleep(2.5)

		# >>> Setting all tablet sensors' orientations to model sensor's orientaiton
		self.tabletSensorOrientationSync()

		# >>> Re-callibrating tablet sensors
		self.tabletSensorReadjust()


if __name__ == '__main__':
	driver()

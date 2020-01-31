import time
import csuRX
import csuDM
import serial


time.sleep(5)
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(5)
timeA = ["Hours", "Minutes", "Seconds"]
gpsD = ["Latitude", "Longitude", "Altitude", "Speed", "TAD", "HD"]
gpsQ = ["Quality", "# of Satellites"]
axis = ["X", "Y", "Z"]
mplA = ["Pressure", "Altitude", "Temperature"]
headers = [timeA, gpsD, gpsQ, axis, axis, axis, mplA]
filenames = ['Time.csv', 'gpsData.csv', 'gpsQuality.csv', 'acc.csv', 'mag.csv', 'gyro.csv', 'mpl.csv']
for i in range(7):
	csuDM.init(filenames[i], headers[i])
csuRX.init()

while True:
	rValue, dString, signalStrength = csuRX.receive()
	dArray = csuDM.deconstruct(dString)
	arduino.write(bytes(dString, 'ascii'))
	i = 0
	for val in dArray:
		csuDM.write(filenames[i], val)
		i += 1
	if rValue:
		print('=' * 60)  # Print a separator line.
		print('Time: {0[0]}:{0[1]}:{0[2]} '.format(dArray[0]))
		print('=' * 60)  # Print a separator line.
		print('Latitude: {0[0]} degrees\nLongitude: {0[1]} degrees\nAltitude: {0[2]} meters\nSpeed: {0[3]} knots\n'.format(dArray[1]))
		print('Fix quality: {0[0]}\n# satellites: {0[1]}'.format(dArray[2]))
		print('=' * 60)  # Print a separator line.
		print('Acceleration (m/s^2): ({0[0]},{0[1]},{0[2]})'.format(dArray[3]))
		print('Magnetometer (uTesla): ({0[0]},{0[1]},{0[2]})'.format(dArray[4]))
		print('Gyroscope (radians/s): ({0[0]},{0[1]},{0[2]})'.format(dArray[5]))
		print('=' * 60)  # Print a separator line.
		print('Pressure: {0[0]} pascals\nAltitude: {0[1]} meters\nTemperature: {0[2]} degrees Celsius'.format(dArray[6]))
		print('=' * 60)  # Print a separator line.	
	time.sleep(0.5)	

	


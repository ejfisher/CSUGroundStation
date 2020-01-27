import time
import busio
import digitalio
import board
import adafruit_rfm9x

def init():
	global rfm9x

	spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)\
	#these board pins may change
	cs = digitalio.DigitalInOut(board.D5) 
	reset = digitalio.DigitalInOut(board.D6)
	try:
		rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
		#remove this later, for testing purposes only
		print("rfm9x module detected!")
	except RuntimeError as error:
		print("Module Not Found")	

def receive():
	rString = ""
	packet = rfm9x.receive()
	if packet is None:
		return False, rString, None
	else:
		print('received raw bytes: {0}'.format(packet))
		rString = str(packet, 'ascii')
		return True, rString, rfm9x.rssi
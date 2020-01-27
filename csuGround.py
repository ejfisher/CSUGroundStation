import time
import csuRX
import csuDM


csuRX.init()

while True:
	rValue, dString, signalStrength = csuRX.receive()
	


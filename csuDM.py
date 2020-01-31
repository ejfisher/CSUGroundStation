


def init(filename, header):
	fstring = ""
	for val in header:
		fstring = fstring + str(val) + ", "
	fstring = fstring[:-2] + "\n"
	f = open("Data/" + filename, 'w')
	f.write(fstring)
	f.close()

def write(filename, dArray):
	fstring = ""
	for val in dArray:
		fstring = fstring + str(val) + ', '
	fstring = fstring[:-2] + '\n'
	f = open("Data/" + filename, 'a')
	f.write(fstring)
	f.close()

def deconstruct(dString):
	itervals = [3, 6, 2, 3, 3, 3, 3]
	padVals = [2, 8, 2, 6, 6, 7, 7]
	dArray = []
	head = 0
	i = 0
	for val in itervals:
		innerArray = [0]*val
		index = 0
		for j in range(val):
			tail = head + padVals[i]
			innerArray[index] = dString[head:tail]
			head = tail
			index += 1
		dArray.append(innerArray)
		i += 1
	return dArray

	


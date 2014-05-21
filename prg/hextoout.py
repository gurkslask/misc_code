def HexToOut(HexVal):
	BinVal = bin(int(HexVal,16))
	bit = []
	for i in range(len(BinVal) - 2):
		print(BinVal[len(BinVal)-1-i])
		bit[i] = BinVal[len(BinVal)-1-i]
	print(bit)

if __name__ == '__main__':
	HexToOut('aa')
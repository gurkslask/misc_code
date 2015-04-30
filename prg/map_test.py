import sys

def celsius(T):
	return (float(5)/9)*(T-32)
temp = (35.6, 34.6)

if __name__ == '__main__':
	a = map(celsius, temp)
	print(a)
	for objects in a:
		print(objects)
	b = map(lambda x: (float(5)/9)*(x-32), temp)
	for objects in b:
		print(objects)
	text = input('Hej: ')
	sys.exit()

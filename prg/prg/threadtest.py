import threading
import time



class test1(threading.Thread):
	def run(self):
		while True:
			print('hej 1')
			time.sleep(2)
class test2(threading.Thread):
	def run(self):
		while True:
			print('hej 2')
			time.sleep(4)

def test3():
	while True:
		print('hej3')
		global var1 
		var1 +=1
		print('inne'+str(var1))
		time.sleep(1)


if __name__ == '__main__':
	var1=42
	print(var1)
	test1().start()
	test2().start()
	threading.Thread(target=test3).start()
	print(var1)



class ExodusTrade:
	def __init__(self):
		
		self.PlayerStash = {'Red' : 0, 'Green' : 0, 'Blue' : 0}
		self.RatioSell2P = {1:5, 2:3}
		self.RatioBuy2P = {1:3, 2:5}
		self.RatioSell3P = {1:5, 2:4, 3:3}
		self.RatioBuy3P = {1:3, 2:4, 3:5}
		self.RatioSell4P = {1:5, 2:4, 3:4, 4:3}
		self.RatioBuy4P = {1:3, 2:4, 3:5, 4:6}
		self.RatioSell5P = {1:5, 2:5, 3:4, 4:3, 5:3}
		self.RatioBuy5P = {1:3, 2:4, 3:4, 4:5, 5:6}		
		self.RatioSell6P = {1:5, 2:5, 3:4, 4:4, 5:3, 6:3}
		self.RatioBuy6P = {1:3, 2:4, 3:4, 4:5, 5:5, 6:6}		

	def CheckIfRightTurn(self):
		assert self.Turn <= len(self.RatioSell), 'Wrong turn'

	def SetRatio(self, Players):
		assert 2 <= Players <= 6, 'Wrong number of players, must be 2-6'
		if Players == 2:
			self.RatioSell = self.RatioSell2P
			self.RatioBuy = self.RatioBuy2P
		elif Players == 3:
			self.RatioSell = self.RatioSell3P
			self.RatioBuy = self.RatioBuy3P

	def SetTurn(self, Turn):
		self.Turn = Turn

	def GetPlayerStash(self):
		return self.PlayerStash

	def SellGreen(self):
		self.CheckIfRightTurn()
		self.PlayerStash['Green'] = self.PlayerStash['Green'] - 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] + self.RatioSell[self.Turn]

	def SellRed(self): 
		self.CheckIfRightTurn()
		self.PlayerStash['Red'] = self.PlayerStash['Red'] - 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] + self.RatioSell[self.Turn]

	def BuyRed(self):
		self.CheckIfRightTurn()
		self.PlayerStash['Red'] = self.PlayerStash['Red'] + 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] - self.RatioBuy[self.Turn]

	def BuyGreen(self, Turn):
		self.CheckIfRightTurn(Turn)
		self.PlayerStash['Green'] = self.PlayerStash['Green'] + 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] - self.RatioBuy[self.Turn]	

	def ClearPlayerStash(self):
		self.PlayerStash = {'Red' : 0, 'Green' : 0, 'Blue' : 0}







def main():
	Test = ExodusTrade()
	Test.SetRatio(2)
	Test.SellGreen(2)
	Test.SellGreen(3)
	print(len(Test.RatioSell))
	print(Test.GetPlayerStash())


if __name__ == '__main__':
	main()
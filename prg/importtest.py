#from Kompensering import Kompensering
from ExodusTrade import ExodusTrade
'''
Test = Kompensering()
Test.SetMax(100)
print(Komp.CountSP(-52))
'''
Test = ExodusTrade()
Test.SetRatio(3)
Test.SellGreen(2)
print(Test.GetPlayerStash())
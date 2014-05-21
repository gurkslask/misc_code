from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import *
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.boxlayout import BoxLayout
from ExodusTrade import ExodusTrade
from kivy.uix.anchorlayout import *
from kivy.uix.floatlayout import *
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

class Exodus(AnchorLayout):
    txt_inpt2 = StringProperty('')
    enint = NumericProperty(1)
    exo = ExodusTrade()
    txt_inpt = StringProperty('')
    act_turn = NumericProperty(0)


    '''
    def __init__(self):
        self.remove_widget(r1)
        self.remove_widget(r2)
        self.remove_widget(r3)
        self.remove_widget(r4)
        self.remove_widget(r5)
        self.remove_widget(r6)
        self.remove_widget(SGreen)        
        self.remove_widget(SRed)        
        self.remove_widget(BGreen)        
        self.remove_widget(Bred)           
    '''
    def init_widget(self):
        pass
        '''self.remove_widget(r1)
        self.remove_widget(r2)
        self.remove_widget(r3)
        self.remove_widget(r4)
        self.remove_widget(r5)
        self.remove_widget(r6)
        self.remove_widget(SGreen)        
        self.remove_widget(SRed)        
        self.remove_widget(BGreen)        
        self.remove_widget(Bred) '''       
    def add_player(self, player):
        '''if player >= 2:
            self.add_widget(r1)
            self.add_widget(r2)
        if player >= 3:
            self.add_widget(r3) 
        if player >= 4:
            self.add_widget(r4)
        if player >= 5:
            self.add_widget(r5)
        if player >= 6:
            self.add_widget(r6)  '''
        pass         
    def add_turn(self, turn):
        '''self.act_turn = turn
        self.add_widget(SGreen)
        self.add_widget(SRed)
        self.add_widget(BGreen)
        self.add_widget(Bred)'''
    def action(self, cmd):
        if cmd == 'bg':
            try:
                self.exo.BuyGreen()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'
        elif cmd == 'br':
            try:
                self.exo.BuyRed()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'
        elif cmd == 'sr':
            try:
                self.exo.SellRed()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'        
        elif cmd == 'sg':
            try:
                self.exo.SellGreen()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'

  




class Buy(Widget):
    size_x = 0
    size_y = 0
    enint2 = NumericProperty(0)
    def coll(self, btn):
        self.remove_widget(btn)
        self.enint2 = self.enint2 + 1
    def draw(self, btn):
        try:
            self.add_widget(btn)
        except:
            pass




class PongApp(App):
    def build(self):
        return Exodus()
if __name__ == '__main__':
    PongApp().run()

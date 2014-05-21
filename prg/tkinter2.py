# -*- coding: cp1252 -*-

import Tkinter

class simpleapp_tk(Tkinter.Tk):#Skapa klass för vårt fönster
	def __init__(self,parent):#Initieringsskit, constructor
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()#Aktivera så gridden

		self.entryVariable = Tkinter.StringVar() #Gör en sträng variabel som vi sätter skriven text i
		self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)#Skapa text ruta som går att skriva i
		self.entry.grid(column=0,row=0,sticky='EW')#Säg var den ska vara i griden
		self.entry.bind('<Return>', self.OnPressEnter)#När vi slår Return så händer OnPressEnter
		self.entryVariable.set(u'Enter text here.')#Sätt texten

		button = Tkinter.Button(self,text=u"Click me !", command=self.OnButtonClick)#Skapa en knapp som kallar på OnButtonClick
		button.grid(column=1,row=0)#Placera knappen i griden

		self.labelvariable = Tkinter.StringVar()#Skapa en variabel som visar text
		label = Tkinter.Label(self,textvariable=self.labelvariable,anchor='w',fg='white',bg='blue')#Gör den fin och säg att den ska titta på labelvariable
		label.grid(column=0,row=1,columnspan=2,sticky='ew')#Placera den i gridden
		self.labelvariable.set(u'Hello!')#En välkomnande text

		self.grid_columnconfigure(0,weight=1)#Gör att knapparna expanderar när fönstret gör det
		self.resizable(True,False)#Blockera horisontell förstoring av fönstret
		self.update()#Förhindra att fönstret ändrar storlek
		self.geometry(self.geometry())#Förhindra att fönstret ändrar storlek
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)#Gör så att textmarkören hamnar på inmatningen efter events


	def OnButtonClick(self):#Skapa en klass för när vi trycker på knappen
		self.labelvariable.set( self.entryVariable.get() + "You clicked the button!")
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)#Gör så att textmarkören hamnar på inmatningen efter events

	def OnPressEnter(self,event):#En klass för när vi slår Return
		#self.labelvariable.set( self.entryVariable.get() +  'You pressed enter!')
		self.CalcIt()
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)#Gör så att textmarkören hamnar på inmatningen efter events

	def CalcIt(self):
		a=self.entryVariable.get()
		if a.isdigit():
			if int(a) % 2 == 0:
				self.labelvariable.set('Even')
			else:
				self.labelvariable.set('Uneven')
		else:
			self.labelvariable.set(a)



if __name__ == "__main__":#Här är vår loop som dunkar igång programmet
	app = simpleapp_tk(None)
	app.title('my application')
	app.mainloop()
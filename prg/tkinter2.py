# -*- coding: cp1252 -*-

import Tkinter

class simpleapp_tk(Tkinter.Tk):#Skapa klass f�r v�rt f�nster
	def __init__(self,parent):#Initieringsskit, constructor
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()#Aktivera s� gridden

		self.entryVariable = Tkinter.StringVar() #G�r en str�ng variabel som vi s�tter skriven text i
		self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)#Skapa text ruta som g�r att skriva i
		self.entry.grid(column=0,row=0,sticky='EW')#S�g var den ska vara i griden
		self.entry.bind('<Return>', self.OnPressEnter)#N�r vi sl�r Return s� h�nder OnPressEnter
		self.entryVariable.set(u'Enter text here.')#S�tt texten

		button = Tkinter.Button(self,text=u"Click me !", command=self.OnButtonClick)#Skapa en knapp som kallar p� OnButtonClick
		button.grid(column=1,row=0)#Placera knappen i griden

		self.labelvariable = Tkinter.StringVar()#Skapa en variabel som visar text
		label = Tkinter.Label(self,textvariable=self.labelvariable,anchor='w',fg='white',bg='blue')#G�r den fin och s�g att den ska titta p� labelvariable
		label.grid(column=0,row=1,columnspan=2,sticky='ew')#Placera den i gridden
		self.labelvariable.set(u'Hello!')#En v�lkomnande text

		self.grid_columnconfigure(0,weight=1)#G�r att knapparna expanderar n�r f�nstret g�r det
		self.resizable(True,False)#Blockera horisontell f�rstoring av f�nstret
		self.update()#F�rhindra att f�nstret �ndrar storlek
		self.geometry(self.geometry())#F�rhindra att f�nstret �ndrar storlek
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)#G�r s� att textmark�ren hamnar p� inmatningen efter events


	def OnButtonClick(self):#Skapa en klass f�r n�r vi trycker p� knappen
		self.labelvariable.set( self.entryVariable.get() + "You clicked the button!")
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)#G�r s� att textmark�ren hamnar p� inmatningen efter events

	def OnPressEnter(self,event):#En klass f�r n�r vi sl�r Return
		#self.labelvariable.set( self.entryVariable.get() +  'You pressed enter!')
		self.CalcIt()
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)#G�r s� att textmark�ren hamnar p� inmatningen efter events

	def CalcIt(self):
		a=self.entryVariable.get()
		if a.isdigit():
			if int(a) % 2 == 0:
				self.labelvariable.set('Even')
			else:
				self.labelvariable.set('Uneven')
		else:
			self.labelvariable.set(a)



if __name__ == "__main__":#H�r �r v�r loop som dunkar ig�ng programmet
	app = simpleapp_tk(None)
	app.title('my application')
	app.mainloop()
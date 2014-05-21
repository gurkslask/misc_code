# -*- coding: cp1252 -*-
import win32clipboard

#Program som gör texten man har i utklipp till små bokstäver

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.EmptyClipboard()
#win32clipboard.CloseClipboard()

data2 = data.lower()
print ('data2')

# set clipboard data
#win32clipboard.OpenClipboard()
win32clipboard.SetClipboardText(data2)
win32clipboard.CloseClipboard()

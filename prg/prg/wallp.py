#!/usr/bin/env 
import os
import random
import time

def main():
	pic_path = '/home/alexander/Pictures/Wallpapers/'
	os.system('gsettings set org.gnome.desktop.background picture-uri file://' + pic_path + random.choice(os.listdir(pic_path)))

if __name__ == '__main__':
	main()
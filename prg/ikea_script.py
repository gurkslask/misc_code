
import requests
from bs4 import BeautifulSoup
import time
import urllib3
from selenium import webdriver
import random

ikea_lista=[
'20205519', #1
'70206012', #1
'60215291', #1
'00204648', #1
'80213432', #1
'40206023', #4
'60221447', #2
'40221448', #3
'80221451', #1
'50215475', #1
'00222831', #1
'90206025', #2
'00206020', #1
'20204633', #1
'40204627', #1
'50204636', #1
'30243295', #1
'50205626', #1
'70208389', #2
'50206027', #1
'90204639', #1
'20221449', #2
'50205626', #1
'50206027', #2
'90204639', #2
'90213568', #1
'70206031', #1
'50244821', #1
'20245186', #1
'70208389', #3
'20221449', #1
'10213572', #1
'60204645', #1
'70213569', #1
'10114218', #1
'40215522', #1
'50206027', #1
'70208389' #2

]




url='http://www.ikea.com/se/sv/catalog/availability/'

with open('text.txt', 'w') as f:	

	for i in ikea_lista:	
	

		url2 = url + i +'/'
		print(url2)	

		
		browser = webdriver.Firefox()
		browser.get(url2)
		html = browser.page_source
		browser.close()
		soup = BeautifulSoup(html)
		k=soup.find(id='findit_box_loc')
		if k.get_text() == '':
			l=soup.find(id= 'graph_main_comment')
			print(i + ' - ' + l.get_text() + ' st \n', file=f)
		else:
			print(i + ' - ' + k.get_text() + '\n', file=f)
		time.sleep(random.randrange(6,14))
#<div class="sc_com_count stock_graph_stock_text">22 st</div>
#findit_box_loc
#findit_shelf_loc
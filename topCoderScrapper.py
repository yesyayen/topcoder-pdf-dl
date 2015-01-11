__author__ = 'anandh'

from bs4 import BeautifulSoup

import urllib2
import pdfkit
import os

class topCoderScrapper:

	def __init__(self):
		
		self.alumni_page=urllib2.urlopen("http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=alg_index")
		self.alumni_data=BeautifulSoup(self.alumni_page.read())


	def convertPage(self):
		base_url = "http://community.topcoder.com"
		for data in self.alumni_data.findAll("td",{'class':'bodyText', 'nowrap':'nowrap'}):
			for url in data.findAll("a"):
				name = url.get_text()
				tmp = url['href']
				file_name = tmp.split('=')[3]
				final_url = base_url+tmp
				
				print "Downloading " + file_name +"...."

				os.system("wkhtmltopdf '"+final_url+"' "+file_name+".pdf")

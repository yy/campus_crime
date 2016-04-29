import bs4
import requests
import datetime
import urllib
import re

class Get_logs(object):
	new_dates = []
	site_links = []
	log_links = []

	
	history = open('data/past_dates.txt', 'r')
	past_dates = history.readlines()
	# print(past_dates)
	history.close()

	def __init__(self):
		self.url_grab()
		self.history_check()
		self.scrapper()


	def url_grab(self):
		# grabs a list of all urls from iupd webpage
		res = requests.get('http://www.indiana.edu/~iupd/dailyLog.html')
		res.raise_for_status()
		website = bs4.BeautifulSoup(res.text, 'html.parser')
		# self.site_links = website.select('li > a')
		for link in website.find_all('a', href=re.compile('Documents/Daily Log/')):
			self.site_links.append(link)
			# print(link)

	def history_check(self):
		# checks to see if date was already anaylzed
		for element in self.site_links:
			element_list = (str(element).split())
			date = element_list[2][4:11]
			if date[-1] == '.':
				date = date[0:6]

			date += '\n'

			if date in self.past_dates:
				pass
			else: 
				self.new_dates.append(date)
				



		log = open('data/past_dates.txt', 'a')
		log.writelines(self.new_dates)
		log.close()
		# print(self.new_dates)

	def scrapper(self):
		for day in self.new_dates:
			day = day.strip('\n')
			input1 = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
			print(input1)
			output = "data/"+day+'.pdf'
			print(output)
			testfile = urllib.URLopener()
			testfile.retrieve(input1, output)


	 


		
	# for link in self.log_links:
	# 	input1 = 'http://www.indiana.edu/~iupd/Documents/Daily%20'+link
	# 	output = "data/"+link[4:15]
	# 	testfile = urllib.URLopener()
	# 	testfile.retrieve('http://www.indiana.edu/~iupd/Documents/Daily%20Log/4-21-16.pdf', output)

Get_logs()

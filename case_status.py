import mechanize
from lxml import html
from bs4 import BeautifulSoup

#this function fetches string for no case condition
def no_case_details():
		#Intializing Browser
		br = mechanize.Browser()

		#Opens url of the form page
		br.open('http://courtnic.nic.in/supremecourt/casestatus_new/caseno_new.asp')	
		
		#Filling & Submitting the form
		br.select_form('caseno')
		br.form['seltype'] = ['2']
		br.form['txtnumber'] = '7575'
		br.form['selcyear'] = ['2016']
		br.submit(name='Submit')	

		#Scrape for required String
		soup = BeautifulSoup(br.response().read().replace('&nbsp',''),'lxml')	#body
		p = soup.findAll('p', attrs={'align':'center'})
		case_details_notfound = p[0].string	#returns no case details found if no record is there
		temp = str(case_details_notfound)

		return temp


#this function catches converted case condition

def converted_condition():
	#Intializing Browser
	br = mechanize.Browser()

	#Opens url of the form page
	br.open('http://courtnic.nic.in/supremecourt/casestatus_new/caseno_new.asp')	
	
	#Filling & Submitting the form
	br.select_form('caseno')
	br.form['seltype'] = ['1']
	br.form['txtnumber'] = '1'
	br.form['selcyear'] = ['2016']
	br.submit(name='Submit')	

	#Scrape for converted case condition
	soup = BeautifulSoup(br.response().read().replace('&nbsp',''),'lxml')	#body
	p = soup.findAll('p')
	if len(p)>0:
		case_details_notfound = p[0].string		#returns no case details found if no record is there
	else:
		case_details_notfound = ''	
	
	temp = str(case_details_notfound)
	no_case_detail = no_case_details()
	
	dictionary = {}		#Initializing the dictionary
	dictionary["is_disposed"] = False

	if temp != no_case_detail:
		#list for converted case
		c = soup.findAll('font', attrs={'face':'verdana'})	
		converted = c[4].string		#gets the converted string
		return converted	
		

def get_case_status(case_type,case_num,year):

	#Intializing Browser
	br = mechanize.Browser()

	#Opens url of the form page
	br.open('http://courtnic.nic.in/supremecourt/casestatus_new/caseno_new.asp')	
	
	#Filling & Submitting the form
	br.select_form('caseno')
	br.form['seltype'] = [str(case_type)]
	br.form['txtnumber'] = str(case_num)
	br.form['selcyear'] = [str(year)]
	br.submit(name='Submit')	

	#Scrape part
	soup = BeautifulSoup(br.response().read().replace('&nbsp',''),'lxml')	#body
	p = soup.findAll('p')
	if len(p)>0:
		case_details_notfound = p[0].string		#returns no case details found if no record is there
	else:
		case_details_notfound = ''	
	
	temp = str(case_details_notfound)
	no_case_detail = no_case_details()
	
	dictionary = {}		#Initializing the dictionary
	dictionary["is_disposed"] = False

	if temp != no_case_detail:
		#list for getting Status and Subject Category
		s = soup.findAll('font', attrs={'name':'verdana'})	
		status = s[0].string	#builds status
		# subject_category = s[1].string.replace('  ','') + '- ' + s[2].string.replace('  ','')	#builds subject category	
		
		#list for getting cause title
		t = soup.findAll('font', attrs={'size':'2'})	
		petitioner = t[5].string.replace('  ','') 
		respondent = t[7].string.replace('  ','')
		
		#list for getting advocate details
		a = soup.findAll('font', attrs={'class':'f12n'})	
		pet_adv = a[2].string.replace('  ','')	#builds pet_adv
		res_adv = a[4].string.replace('  ','')	#builds res_adv

		#list for converted case
		c = soup.findAll('font', attrs={'face':'verdana'})	
		converted = c[4].string		#gets the converted string
		converted_case_dictionary = {}
		b = converted_condition()
			
		if(status == 'DISPOSED'):
			dictionary["is_disposed"] = True
			
		dictionary["petitioner"] = petitioner
		dictionary["respondent"] = respondent
		dictionary["pet_advocate"] = pet_adv
		dictionary["res_advocate"] = res_adv

		if converted != b:
			converted_case_dictionary["case_num"]= case_num
			converted_case_dictionary["year"] = year
		
		dictionary["converted_case"] = converted_case_dictionary		
	elif temp == no_case_detail:
		dictionary["petitioner"] = 'Not Available'
		dictionary["respondent"] = 'Not Available'
		dictionary["pet_advocate"] = 'Not Available'
		dictionary["res_advocate"] = 'Not Available'
		dictionary["converted_case"] = {}
	
	return dictionary

	
		
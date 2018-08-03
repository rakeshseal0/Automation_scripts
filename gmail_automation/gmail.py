#By Rakesh Seal

'''''''''
								INSTRUCTIONS
 1.Email body ----> in body.txt
 2.Edit Subject below in script
 3.name of the attachments should be: "brochure.pdf"  and "poster.pdf"
 4.Edit gmail credentials before use in script
 5.name of the csv file should be:   "excel_email.csv" and emails will be in 1st row
'''''''''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
import sys

email="xxxxxxxx3@gmail.com"       							#login credentials
password="passpasspass"


subject="Invitation for participation and promotion"            #Email subject

filepath=str(sys.path[0])+"/attachments/brochure.pdf"									#path for attachment
filepath1=str(sys.path[0])+"/attachments/poster.pdf"




#temp variables 
email_arr=[]               #for appending emails from csv
body=""                    #from txt to string 
recpnt_string=""           #email to string

driver=None




def csv_to_str():
	global recpnt_string
	filename='excel_email.csv'
	with open(filename) as csvfile:
		reader=csv.reader(csvfile)
		try:
			for row in reader:
				email_arr.append(row)
		except csv.ERROR as e:
			sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

		print("Sending mail to:")
		for e in range(0,len(email_arr)):
			email=""
			email=str(email_arr[e]).replace("['","").replace("']","")
			recpnt_string += email+","
			print(email)
		
		

def body():
	print("\n\nsubject:\n"+subject)
	global body
	b=open("body.txt","r")
	body=str(b.read())
	print("\nBody:\n"+body)

def aggree():
	agg=input("Please read the recipient and body\n Y to send Q to quit:\n")
	if(agg=="Y" or agg=="y"):
		pass
	else:
		print("permission denied")
		sys.exit()


def browser_start():
	global driver
	driver=webdriver.Chrome(executable_path="/home/rakesh/py/selenium_drivers/chromedriver")


def get_gmail():
	try:
		driver.get("https://mail.google.com/mail/u/0/h/4mk826itq4cr/?&cs=b&pv=tl&v=b")
	except:
		print("Network Error")
		sys.exit()


def login():
	driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email+Keys.ENTER)
	time.sleep(3)
	driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/div[1]/div/div[1]/div/div[1]/input').send_keys(password+Keys.ENTER)



def send_mail():
	print("Loading..")
	time.sleep(5)
	driver.find_element_by_xpath('//*[@id="to"]').send_keys(recpnt_string+Keys.ENTER)
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[4]/td[2]/input').send_keys(subject)          #subject
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[8]/td[2]/textarea').send_keys(body)          #body text



	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[6]/td[2]/input').send_keys(filepath)         #attachment1
	time.sleep(5)
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[7]/td[2]/input').click()
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[3]/tbody/tr[2]/td[2]/input').send_keys(filepath1)             #attachment2
	time.sleep(5)
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/input[1]').click()

	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[3]/tbody/tr/td/input[1]').click()                        #send button
	time.sleep(5)
	print("sucessfully sent :)")


if __name__ == '__main__':
	csv_to_str()
	body()
	aggree()
	browser_start()
	get_gmail()
	login()
	send_mail()
	driver.quit()

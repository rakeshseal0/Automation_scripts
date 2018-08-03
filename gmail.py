from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver=None

email="xxxxxxx"       #login credentials
password="xxxxxx"


recpnt=["rakeshseal0@gmail.com","rakeshseal8@gmail.com","ieminnovare@gmail.com"]         #email credentials
subject="s test"
body="testing s 1"
recpnt_string=""



def browser_start():
	global driver
	driver=webdriver.Chrome(executable_path="/home/rakesh/py/selenium_drivers/chromedriver")


def get_gmail():
	driver.get("http://www.gmail.com")

def login():
	driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email+Keys.ENTER)
	time.sleep(1.5)
	driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/div[1]/div/div[1]/div/div[1]/input').send_keys(password+Keys.ENTER)

def recpt_list():
	global recpnt_string
	print("Sending mail to:")
	for i in range(0,len(recpnt)):
		print(recpnt[i])
		recpnt_string += recpnt[i]+","



def send_mail():
	print("Loading..")
	time.sleep(5)
	driver.get("https://mail.google.com/mail/u/0/h/4mk826itq4cr/?&cs=b&pv=tl&v=b")
	driver.find_element_by_xpath('//*[@id="to"]').send_keys(recpnt_string+Keys.ENTER)
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[4]/td[2]/input').send_keys(subject)
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[8]/td[2]/textarea').send_keys(body)
	driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[3]/tbody/tr/td/input[1]').click()
	time.sleep(5)
	print("sucessfully sent :)")


if __name__ == '__main__':
	browser_start()
	get_gmail()
	login()
	recpt_list()
	send_mail()

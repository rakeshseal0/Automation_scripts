from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random

target='IEDC 2018'       #name of sir saved in your phone
driver=None
n=50

'''
use msg list for sending multiple message
will be selected randomly
one msg for default
'''
msg=['SOHAN SIR KHAWAN']#['Sir khawan',' sir khawabe','sir khawatei hbe','sir khawachche','sir khawaben']         #increase it for twist   
            

def load():
	global driver
	driver=webdriver.Chrome(executable_path="/home/rakesh/rak3sh/py/chromedriver")
	
def login():
	driver.get("https://web.whatsapp.com/")
	while True:
		time.sleep(0.5)
		try:
			if driver.find_element_by_xpath("//*[@id='app']/div/div/div[3]/div/div/div[1]"):
				#seach
				print("login")
				time.sleep(5)
				break
		except NoSuchElementException:
				pass
		finally:
				print("Trying to log in  scan qr")


def search():
		inputElem=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input').send_keys(target,Keys.RETURN)
		
def send(i):
	print("annoyed "+str(i)+" times")
	i=random.randint(1,len(msg))

	driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg[i-1],Keys.RETURN)
	time.sleep(0.1)
def quit():
	time.sleep(1)
	driver.quit()


if __name__ == '__main__':
	load()
	login()
	search()

	for i in range(0,n):        #100 times texing :)
		send(i)
	
	quit()


	

	
	

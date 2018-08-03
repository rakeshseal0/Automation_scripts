from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

driver=None
flag=False

username='9733028233'
password='xxxxx'

tgt='7001462761'
mssg='vjvdgfqwvjhbfskhdb'


def load():
	global driver
	driver=webdriver.Firefox(executable_path="/home/rakesh/py/selenium_drivers/geckodriver")


def login(user,passw):
	driver.get('http://www.way2sms.com/content/index.html?')
	driver.find_element_by_xpath('//*[@id="username"]').send_keys(user)
	driver.find_element_by_xpath('//*[@id="password"]').send_keys(passw)
	driver.find_element_by_xpath('//*[@id="loginBTN"]').click()
	while(1):
		try:
			if driver.find_element_by_xpath('//*[@id="mlocator"]'):
				flag=True
				print('logged in')
				time.sleep(1.5)
				break
		except NoSuchElementException:
			time.sleep(1)
			pass
		finally:
			if (flag==False):
				print('Trying to login')
			else:
				print('.')
def sendSms(target,msg,t):					#takes 3 argument target_no(str),text(str),dump no(int)
	flag1=False
	while(1):

		try:

			driver.find_element_by_xpath('//*[@id="sendSMS"]/a').click()
			time.sleep(1)
			driver.switch_to_frame("frame")
			driver.find_element_by_xpath('//input[@name="mobile"]').send_keys(target)
			driver.find_element_by_xpath('//*[@id="message"]').send_keys(msg)
			driver.find_element_by_xpath('//*[@id="Send"]').click()
		except NoSuchElementException:
			pass
			flag1=True
		finally:
			if (flag1!=True):
				print('sms sent '+str(t+1)+' times')
				break
			else:
				print('sms not sent')
				time.sleep(1)

def spam(t):
	for i in range(0,t):
		sendSms(tgt,mssg,i)


if __name__ == '__main__':
	load()
	login(username,password)
	spam(1)               #no of times you want to send text      

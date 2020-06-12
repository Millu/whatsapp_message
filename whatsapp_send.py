from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time, csv


def send_notice():
	try:
		driver.get("https://api.whatsapp.com/send?phone="+number)
		wait = WebDriverWait(driver, 600) 

		new_msg_button = "//*[@id='action-button']"
		new_message = wait.until(EC.presence_of_element_located(( 
		    By.XPATH, new_msg_button))) 
		new_message.click()
		time.sleep(10)

		##click attachement button
		attachment_button = "//div[@id='main']/header/div[3]/div/div[2]/div"
		attachment_menu = wait.until(EC.presence_of_element_located(( 
		    By.XPATH, attachment_button))) 
		attachment_menu.click()
		time.sleep(3)

		### attach photo
		photos_video_button = "//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input"
		photos_video = wait.until(EC.presence_of_element_located(( 
		    By.XPATH, photos_video_button)))
		photos_video.send_keys(file_path)
		time.sleep(3)

		## write caption & send message
		caption_field = "//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]"
		caption_find = wait.until(EC.presence_of_element_located(( 
		    By.XPATH, caption_field)))
		if message_content != '':
			caption_find.send_keys(message_content)
		caption_find.send_keys(Keys.ENTER)
		
		time.sleep(10)
		print('sent,'+number)
	except Exception as e:
		print(e)
		print('error,'+number)
	finally:
		pass

with open('numbers/morning_evening.csv') as cfile:
	reader = csv.reader(cfile, delimiter=',')
	morning_evening = [row[0] for row in reader]

with open('numbers/evening.csv') as cfile:
	reader = csv.reader(cfile, delimiter=',')
	evening = [row[0] for row in reader]

with open('numbers/validation.csv') as cfile:
	reader = csv.reader(cfile, delimiter=',')
	validation = [row[0] for row in reader]	

with open('numbers/cummalative_morning_evening.csv') as cfile:
	reader = csv.reader(cfile, delimiter=',')
	cumma = [row[0] for row in reader]	



message_content = ""
file_path = ""

count = 0
number_set = cumma[count:]

driver = webdriver.Chrome('') 
for number in number_set:
	print(count)
	send_notice()
	count += 1


# driver.quit()

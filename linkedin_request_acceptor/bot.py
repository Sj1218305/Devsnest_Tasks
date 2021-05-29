from selenium import webdriver
import time
import os
# from webdriver_manager.chrome import ChromeDriverManager


LINKEDIN_EMAIL = os.environ['LINKEDIN_EMAIL']
LINKEDIN_PASSWORD = os.environ['LINKEDIN_PASSWORD']

# driver = webdriver.Chrome(ChromeDriverManager().install())


PATH = "/home/jain/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com")
driver.maximize_window()

def accept():
	input_email = driver.find_element_by_id("session_key")
	input_email.send_keys(LINKEDIN_EMAIL)
	input_pswd = driver.find_element_by_id("session_password")
	input_pswd.send_keys(LINKEDIN_PASSWORD)
	sign_in = driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")
	sign_in.click()
	driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
	accept = []
	while len(accept)==0:
		accept = driver.find_elements_by_xpath("//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
	
	for button in accept:
		button.click()

	print("Done")		

accept()
# connect python with webbrowser-chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException        

def check_exists_by_xpath(browser,xpath):

    try:

        browser.find_element(By.XPATH,xpath)

    except NoSuchElementException:

        return False

    return True
def check_exists(element,browser,sel):

    try:

        browser.find_element(element,sel)

    except NoSuchElementException:

        return False

    return True
plinks=pd.read_csv("linkedin_extracted_links.csv")

first_column = list(plinks. iloc[1:, 0] )

s=Service('chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = "http://linkedin.com/"

        # path to browser web driver		
browser.get(url)


# Getting the login element
username = browser.find_element(By.ID,"session_key")

# Sending the keys for username	
username.send_keys("username")

# Getting the password element								
password = browser.find_element(By.ID,"session_password")

# Sending the keys for password
password.send_keys("password")	

# Getting the tag for submit button					
browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()


sleep(2)

text="Your personalised note goes here :)"
for i in first_column:
    browser.get(i)

    
    xpath="//main[@id='main']/div[1]/section[1]/div[2]/div[3]/div[1]/button[1]/span[1]"

    if check_exists_by_xpath(browser,xpath):
        browser.find_element(By.XPATH,xpath).click()
        if check_exists(By.ID,browser,"custom-message"):
            browser.find_element(By.ID,"custom-message").send_keys(text)
            browser.find_element(By.CSS_SELECTOR,"[aria-label='Send now']").click()
    else:
        browser.find_element(By.CSS_SELECTOR,"[aria-label='More actions']").click()
        if check_exists(By.CSS_SELECTOR,browser,"[data-control-name='follow']"):
            browser.find_element(By.CSS_SELECTOR,"[data-control-name='follow']").click()
    sleep(3)
    print("Done")


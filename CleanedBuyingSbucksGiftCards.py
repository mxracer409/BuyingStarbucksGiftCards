import sys
import time
import requests
from requests_html import HTMLSession
#from bs4 import BeautifulSoup
#from urllib.parse import urljoin
import json
import re
import selenium
from selenium import webdriver
#from getpass import getpass

def loadGiftCards(path):
    #load in the giftcard data
    with open(path) as f:
        giftCardsToBuy = json.load(f)
    return giftCardsToBuy


#def loginToSbucks(username, password):
def getCreds():
    #username = input('Enter the Starbucks username: ')
    #print('Enter the Starbucks password')
    #password = getpass()

    return

def connectToSbucks():
    driver = webdriver.Chrome(executable_path='D:/Python/webdrivers/chromedriver_win32/chromedriver.exe')
    url = "https://www.starbucks.com/gift/873070232"
    driver.get(url)
    return driver
    
#def temp():

def populateForm():
    return

def main():
    loadGiftCards('jsondata.json')
    getCreds()
    #connectToSbucks()
    populateForm()
    return 

#if __name__ == "__main__":
#   main()



#Setting the Chromium web browser options to load the user profile data - This allows us to leverage the "autofill" and saved passwords
#for websites
cOptions = webdriver.ChromeOptions()
cOptions.add_argument("user-data-dir=C:/Users/Justin/AppData/Local/Chromium/User Data")

#Creating the webdriver for browser chrome and assiging it to driver variable
driver = webdriver.Chrome(executable_path='D:/Python/webdrivers/chromedriver_win32/chromedriver.exe',chrome_options=cOptions)

#note - this section was attempting to automate the sign in procedure but Starbucks sign in page i think is using a java script
#that I cant figure out which one and the sign in process would not take when entered with code... but same browser session would work
#if entered manually with keyboard. Thus the path to figure out how to load saved user profile data of the browser and avoid having
#to fillin the username and password fields. 

#clicking the SignIn button
#driver.find_element_by_xpath('/html/body/div[2]/header/nav/div[1]/div/div[2]/div[2]/div/a[2]').click()

#Entering the information on the sign in page - Notice to for loop trying to send key board input for java script
#to pickup as entering the whole field was not allowing the successfull authentication
#driver.find_element_by_id('username').click()
#time.sleep(1)
#username = '<username>'
#for char in username:
#    driver.find_element_by_id('username').send_keys(char)
#password = '<password>'
#driver.find_element_by_id('password').click()
#time.sleep(1)
#for char in password:
#    driver.find_element_by_id('password').send_keys(char)
#time.sleep(1)
#click the sign in button
#driver.find_element_by_xpath('//*[@id="content"]/div[2]/span[2]/div/div[1]/form/div[6]/div/span/div/button').click()

#driver.find_element_by_css_selector('#content > div.sb-contentCrate.passOnFullHeight___3Lo2I > span.block.height-100 > div > div.sb-contentColumn.mx-auto.sb-contentColumn--narrow.pb5 > form > div.invisible.sb-global-gutters.py3.lg-py5.base___3dWsJ.md___X7jh3 > div > span > div > button').click()


#load giftCardData
with open('jsondata.json') as f:
    giftCardsToBuy = json.load(f)

#Enter in the form data
for giftcard in giftCardsToBuy:

    url = "https://www.starbucks.com"
    driver.get(url)
    time.sleep(3)
    
    #click the gift cards tab at the top
    driver.find_element_by_xpath('/html/body/div[2]/header/nav/div[1]/div/div[2]/div[1]/ul/li[3]/a').click()
    #click the "Happy Holidays card"
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/main/div/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/a').click()

    time.sleep(2)
    driver.find_element_by_id('amount').click()
    #This hard selects the $10 gift card
    #driver.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/span[2]/div/form/div[2]/div[1]/div[1]/select/option[2]').click()

    #This selects the correct amount based on gift card amount JSON value
    #These are the values from the website drop down menu
    #custom is not used here
    #amount > option:nth-child(2) = $10
    #amount > option:nth-child(3) = $25
    #amount > option:nth-child(4) = $50
    #amount > option:nth-child(5) = $100
    #amount > option:nth-child(6) = custom amount and adds new field to fill in
    #print(giftCardsToBuy[giftcard]["amount"])
    #print(giftCardsToBuy["giftCard1"]["amount"])
    

    if giftCardsToBuy[giftcard]["amount"] =='$10':
        driver.find_element_by_css_selector('#amount > option:nth-child(2)').click()
    elif giftCardsToBuy[giftcard]["amount"] =='$25':
        driver.find_element_by_css_selector('#amount > option:nth-child(3)').click()
    elif giftCardsToBuy[giftcard]["amount"] =='$50':
        driver.find_element_by_css_selector('#amount > option:nth-child(4)').click()
    elif giftCardsToBuy[giftcard]["amount"] =='$100':
        driver.find_element_by_css_selector('#amount > option:nth-child(5)').click()
    elif giftCardsToBuy[giftcard]["amount"] =='custom':
        pass
        #driver.find_element_by_css_selector('#amount > option:nth-child(6)').click()
    

    #fill in the recipient details
    driver.find_element_by_id('recipientEmail').clear() #clears the autofill from user profile of browser
    driver.find_element_by_id('recipientEmail').send_keys(giftCardsToBuy[giftcard]["recipientEmail"])
    driver.find_element_by_id('recipientName').clear() #clears the autofill from user profile of browser
    driver.find_element_by_id('recipientName').send_keys(giftCardsToBuy[giftcard]["recipientName"])

    driver.find_element_by_id('senderEmail').clear() #clears the autofill from user profile of browser
    driver.find_element_by_id('senderEmail').send_keys(giftCardsToBuy[giftcard]["senderEmail"])
    driver.find_element_by_id('senderName').clear() #clears the autofill from user profile of browser
    driver.find_element_by_id('senderName').send_keys(giftCardsToBuy[giftcard]["senderName"])

    #This is the Checkout Button that pops up on the new frame at the bottom of the page. 
    driver.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/span[2]/div/form/div[9]/div/span/div/button').click()

    #This is the "Send Gift" that pops up on the new frame at the bottom of the page while validating your CC info
    #YOU WILL NEED TO UNCOMMENT THIS LINE TO ACTUALY SUBMITT THE ORDER
    time.sleep(2)
    #driver.find_element_by_css_selector('div.visible:nth-child(2) > button:nth-child(1)').click()

from selenium import webdriver
import getpass
import time
uName = input("Enter Discord Username :")
uPwd = getpass.getpass("Enter PWD :")
url = input("Enter Server Channel Url")
if (url.startswith("https://"))  :
    browser = webdriver.Chrome(executable_path='C:/Chrome-Web-Driver/chromedriver.exe')
    browser.get(url)


else  :
    print ("URL invalid")
 




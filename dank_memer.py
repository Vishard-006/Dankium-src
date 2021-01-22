from selenium import webdriver
import getpass
import time
driver_path = input("Enter Chrome Web-Driver Path  : ")
uName = input("Enter Discord Username / Email :")
uPwd = getpass.getpass("Enter PWD :")
url = input("Enter Server Channel Url:")
if (url.startswith("https://discord.com/"))  :
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    

else  :
    print ("URL invalid")
 




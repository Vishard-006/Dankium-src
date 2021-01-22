from selenium import webdriver
import getpass
import time

uName = input("Enter Discord Username / Email :")
uPwd = getpass.getpass("Enter PWD :")
url = input("Enter Server Channel Url:")
if (url.startswith("https://discord.com/"))  :
    driver = webdriver.Chrome(executable_path='C:\Chrome-Web-Driver\chromedriver.exe')
    driver.get(url)
    email = driver.find_element_by_name('email')
    email.send_keys(uName)
    password = driver.find_element_by_name('password')
    password.send_keys(uPwd)
    login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
    login_button.click()
    

else  :
    print ("URL invalid")
 




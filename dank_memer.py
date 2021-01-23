from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
import random
import os.path
import json



if os.path.isfile("./data.json") :
    y = input("Load saved Login ? y/n ?") 
    if y=='y' :
        f = open("./data.json")
        data = json.loads(f.read())
        uName = data["Name"]
        uPwd = data["PWD"]
        url = data["url"]
    else :
        uName = input("Enter Discord Username / Email :")
        uPwd = getpass.getpass("Enter PWD :")
        url = input("Enter Server Channel Url:")

else :
    x = input("want to save login credentials (credentials will be stored at ./data.json) ? y/n ?")
    if x=='y' :     
            uName = input("Enter Discord Username / Email :")
            uPwd = getpass.getpass("Enter PWD :")
            url = input("Enter Server Channel Url:")
            f = open("usr.json", "a+")
            f.write("{")
            f.write("\n")
            f.write('"Name"')
            f.write(" : ")
            f.write('"x" ,')
            f.write("\n")
            f.write('"PWD"')
            f.write(" : ")
            f.write('"y" ,')
            f.write("\n")
            f.write('"url"')
            f.write(" : ")
            f.write('"z"')
            f.write("\n")
            f.write("}")
           
            f = open("./usr.json" , "a+")
            data = json.loads(f.read())
            data["Name"] = uName
            data["PWD"] = uPwd
            data["url"] = url
            
            f.close()
            os.remove("./usr.json")
            d = open("data.json" , "a+")
            json.dump(data, d)
            
    else :
         uName = input("Enter Discord Username / Email :")
         uPwd = getpass.getpass("Enter PWD :")
         url = input("Enter Server Channel Url:")






if (url.startswith("https://discord.com/")):
    xPath ='//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div[1]/div/div/div/div[1]/div[2]'
    a = input("By default this bot will post to Friends Hangout . Post somewhere else ?")
    if a=='y' :
        xPath = input("Go to your browser dev tools , click select by element and click on message input box and select copy xpath. Now paste that value here :")
    driver = webdriver.Chrome(executable_path=r'C:\Chrome-Web-Driver\chromedriver.exe')
    driver.get(url)
    email = driver.find_element_by_name('email')
    email.send_keys(uName)
    password = driver.find_element_by_name('password')
    password.send_keys(uPwd)
    
    login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
    login_button.click()
    time.sleep(15)
    msg = driver.find_element_by_xpath(xPath)
    print ("This program will run on an infinite loop . Press CTRL+C anytime to stop")
    
    
    while True :
        msg.send_keys("pls beg")
        msg.send_keys(Keys.RETURN)
        time.sleep(6)
        msg.send_keys("pls dep all")
        msg.send_keys(Keys.RETURN)
        time.sleep(6)
        msg.send_keys("pls hunt")
        msg.send_keys(Keys.RETURN)
        time.sleep(6)
        msg.send_keys("pls fish")
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        memes = ['f' , 'r' , 'i' , 'c' , 'k']
        pm = random.choice(memes)
        msg.send_keys("pls pm")
        msg.send_keys(Keys.RETURN)
        time.sleep(6)
        msg.send_keys(pm)
        msg.send_keys(Keys.RETURN)
        time.sleep(6)
        msg.send_keys("pls dep all")
        msg.send_keys(Keys.RETURN)
        time.sleep(6)
        time.sleep(6)

else  :
    print ("URL invalid")
 
#TODO  pls search




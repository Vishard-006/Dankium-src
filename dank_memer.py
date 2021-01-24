from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
import random
import os.path
from os import system, name
import json

system("cls")

if os.path.isfile("./data.json") :
    y = input("Load saved Login ? y/n ?") 
    if y=='y' :
        f = open("./data.json")
        data = json.loads(f.read())
        uName = data["Name"]
        uPwd = data["PWD"]
        url = data["url"]
        brw = data["brw"]
        
    else :
        uName = input("Enter Discord Username / Email :")
        uPwd = getpass.getpass("Enter PWD :")
        url = input("Enter Server Channel Url:")
        brw = input("Chrome (c) or Firefox (f) ?")
        
else :
    x = input("want to save login credentials (credentials will be stored at ./data.json) ? y/n ?")
    if x=='y' :     
            uName = input("Enter Discord Username / Email :")
            uPwd = getpass.getpass("Enter PWD :")
            url = input("Enter Server Channel Url:")
            brw = input("Chrome (c) or Firefox (f) ?")
            
            data = {
                "Name" : "x",
                "PWD" : "y",
                "url" : "z",
                "brw" : "v"
                
            }
            
            data["Name"] = uName
            data["PWD"] = uPwd
            data["url"] = url
            data["brw"] = brw
            
            d = open("data.json" , "a+")
            json.dump(data, d)
            d.close()
            
    else :
         uName = input("Enter Discord Username / Email :")
         uPwd = getpass.getpass("Enter PWD :")
         url = input("Enter Server Channel Url:")
         brw = input("Chrome (c) or Firefox (f) ?")
         driPath = input("Path for webdriver:")






if (url.startswith("https://discord.com/")):
    system("cls")
    xPath ='//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div[1]/div/div/div/div[1]/div[2]'
   
    
    if brw=='c' :
        driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
    elif brw=="f" :
        driver = webdriver.Firefox(executable_path=r"./geckodriver.exe")
    driver.get(url) 
    system("cls")
    email = driver.find_element_by_name('email')
    email.send_keys(uName)
    password = driver.find_element_by_name('password')
    password.send_keys(uPwd)
    
    login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
    login_button.click()
    time.sleep(40)
    msg = driver.find_element_by_xpath(xPath)
    system("cls")
    print ("Logged in Succesfully . This program will run on an infinite loop . Press CTRL+C anytime to stop")
    
    
    while True :
        msg.send_keys("pls beg")
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        msg.send_keys("pls dep all")
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        msg.send_keys("pls hunt")
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        msg.send_keys("pls fish")
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        memes = ['f' , 'r' , 'i' , 'c' , 'k']
        pm = random.choice(memes)
        msg.send_keys("pls pm")
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        msg.send_keys(pm)
        msg.send_keys(Keys.RETURN)
        time.sleep(7)
        msg.send_keys("pls dep all")
        msg.send_keys(Keys.RETURN)
        time.sleep(8)
        
        time.sleep(10)

else  :
    print ("URL invalid")
 




##
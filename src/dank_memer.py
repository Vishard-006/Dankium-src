from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
import random
import os.path
from os import system, name
import json
import tkinter
#added nothing
#another watse comment
if os.path.isfile("./data.json") :
    y = input("Load saved Login ? y/n ?") 
    if y=='y' :
        try :
            f = open("./data.json")
        except :
            print("run as admin . ")
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
            try :
                with open('data.json', "a+") as d:
                    json.dump(data, d)
                    d.close()
            except :
                print("Dont have perms")
            
    else :
         uName = input("Enter Discord Username / Email :")
         uPwd = getpass.getpass("Enter PWD :")
         url = input("Enter Server Channel Url:")
         brw = input("Chrome (c) or Firefox (f) ?")
         






if (url.startswith("https://discord.com/")):
    system("cls")  
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
    try :
        login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
        login_button.click()
        driver.implicitly_wait(60)
    except :
        print("Login Unsuccesful . Please enter correct credentials")
    else :
        msg = driver.find_element_by_css_selector(".markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP")
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
    





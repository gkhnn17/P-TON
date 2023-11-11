from instagramUserInfo import userName,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class Instagram:
    def __init__(self,userName,password):
        #set eng
        self.driverProfile =webdriver.ChromeOptions()
        self.driverProfile.add_experimental_option('prefs',{'intl.accept_languages' :'en,en_US' })
        #opening
        self.driver = webdriver.Chrome('chromedriver.exe',options=self.driverProfile)
        self.userName =userName
        self.password=password
       

    def signIn(self):
        self.driver.get("https://instagram.com")
        time.sleep(3)


        searchName = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.userName)
        searchPassword = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)

    def getFollowers(self):
        self.driver.get(f"https://instagram.com/{self.userName}")
        time.sleep(2)
        
        followers_link = self.driver.find_element(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd')

        # Click the followers link
        followers_link.click()
        time.sleep(3)

        # Wait for the followers list to load
        time.sleep(2)

        # Locate the container element
        container = self.driver.find_element(By.XPATH, "//div[@class='_aano']")

        last_height = self.driver.execute_script("return arguments[0].scrollHeight;", container)
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)
            time.sleep(1)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight;", container)
            if new_height == last_height:
                break
            last_height = new_height

        # Retrieve the followers
        followers = self.driver.find_elements(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd')

        followerList =[]
        i= 0
        
        for follower in followers:
            href = follower.get_attribute('href')
            print(href)
            time.sleep(0.2)
            followerList.append(href)
            i+=1
            print(i)
        
        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item +"\n")
                time.sleep(0.5)



    def followeUser(self,username):
        self.driver.get("https://www.instagram.com/"+username)
        time.sleep(2)

        followButton =self.driver.find_element(By.TAG_NAME,"button")
        if followButton != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("zaten takiptesin")

    def unFollowUser(self,username):
        self.driver.get("https://www.instagram.com/"+username)
        time.sleep(2)

        followButton =self.driver.find_element(By.TAG_NAME,"button")
        if followButton.text =="Following":
            followButton.click()
            time.sleep(2)
            confirmButton = self.driver.find_element(By.XPATH,'//button[text()="Unfollow"]').click()
        else:
            print("takipte değilsin zaten")

instagram = Instagram(userName, password)
instagram.signIn()
instagram.getFollowers()
#instagram.followeUser("kod_evreni")
#instagram.unFollowUser('kod_evreni')
exit = input("Do you want to exit ?:")
instagram.driver.quit()

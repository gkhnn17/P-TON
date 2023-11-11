from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_langugaes': 'en,en_US}'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.password = password
        self.username = username

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(10)


twitter =Twitter(username,password)
twitter.signIn()
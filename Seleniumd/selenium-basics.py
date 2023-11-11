from selenium import webdriver
import time

driver = webdriver.Chrome()

url = " http://github.com"
driver.get(url)

time.sleep(2)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("github.com-home.png")

url = "https://github.com/gkhnn17"
print(driver.title) 
if "sadik turan" in driver.title:
    driver.save_screenshot("github-sadikturab.png")

driver.back()
time.sleep(2)

time.sleep(2)
driver.close()
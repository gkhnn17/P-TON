from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url="http://github.com"
driver.get(url)


searchInput = driver.find_element(By.NAME,"q")#name
searchInput = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")#xpath
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
"""
result=driver.page_source
"""
result =driver.find_elements(By.CSS_SELECTOR,"li.repo-list-item a ")#href

for element in result:
    print(element.text)
driver.close()
#***************************Bot kurulumu*****************************

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.instagram.com/"

driver.get(url)

# Wait for a specified amount of time (in seconds) before closing the window
time.sleep(5)  # Wait for 5 seconds

# Close the window
driver.quit()
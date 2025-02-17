import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/M0NS13UR-K")
title = driver.title

time.sleep(1)

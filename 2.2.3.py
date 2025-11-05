from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Имя")
    browser.find_element(By.NAME, "lastname").send_keys("Фамилия")
    browser.find_element(By.NAME, "email").send_keys("ty@mail.ru")
    browser.find_element(By.NAME, "file").send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()



finally:
    time.sleep(10)
    browser.quit()
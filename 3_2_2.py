from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def start_browser(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input1.send_keys("this is a must!")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input2.send_keys("this is a must!")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input3.send_keys("this is a must!")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    return welcome_text

class TestAbs(unittest.TestCase):
    def test_html1(self):
        self.assertEqual(start_browser("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "Should be equal")

    def test_html2(self):
        self.assertEqual(start_browser("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "Should be equal")

if __name__ == "__main__":
    unittest.main()
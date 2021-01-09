from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
    
        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//*[@class='first_block']/div[1]/input")
        input1.send_keys("Maks")
        input2 = browser.find_element_by_xpath("//*[@class='first_block']/div[2]/input")
        input2.send_keys("Huis")
        input3 = browser.find_element_by_xpath("//*[@class='first_block']/div[3]/input")
        input3.send_keys("gmilo@gmilo.hre")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = browser.find_element_by_tag_name("h1").text
 
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    
    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
    
        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//*[@class='first_block']/div[1]/input")
        input1.send_keys("Maks")
        input2 = browser.find_element_by_xpath("//*[@class='first_block']/div[2]/input")
        input2.send_keys("Huis")
        input3 = browser.find_element_by_xpath("//*[@class='first_block']/div[3]/input")
        input3.send_keys("gmilo@gmilo.hre")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = browser.find_element_by_tag_name("h1").text
       
            
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()

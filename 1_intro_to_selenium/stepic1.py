from selenium import webdriver
import time







# В этой функции мы вставляем все поля (обязательные и необязательные)
try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first_name = browser.find_element_by_class_name("first")
        first_name.send_keys("Ivan")

        last_name = browser.find_element_by_class_name("second")
        last_name.send_keys("Ivanov")

        email = browser.find_element_by_class_name("third")
        email.send_keys("1@gmail.com")

        telephone = browser.find_element_by_xpath("//input[@placeholder = 'Input your phone:']")
        telephone.send_keys("77777777777")

        address = browser.find_element_by_xpath("//input[@placeholder = 'Input your address:']")
        address.send_keys("Wall street")

        button = browser.find_element_by_class_name("btn")
        button.click()
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

finally:
        browser.quit()




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()
    
    # считываем икс
    x = browser.find_element_by_xpath("//*[@id='input_value']").text
    
    # вычисляем f(x)
    y = str(math.log(abs(12*math.sin(int(x)))))

    # записываем значение функции в поле
    browser.find_element_by_xpath("//*[@id='answer']").send_keys(y)

    # отправляем решение 
    browser.find_element_by_xpath("//*[@type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка







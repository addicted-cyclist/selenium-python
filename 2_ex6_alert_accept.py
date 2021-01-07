from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # нажимаем на go on magical journey
    browser.find_element_by_xpath("//*[@type='submit']").click()
    
    # подтверждаем модальное окно
    confirm = browser.switch_to.alert
    confirm.accept()
    
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

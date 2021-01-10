from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #считываем значение a и b
    a = browser.find_element_by_xpath("//*[@id='num1']").text
    b = browser.find_element_by_xpath("//*[@id='num2']").text
    
    #вычисляем сумму 
    y = str(int(a)+int(b))
    
    #найти пункт списка с правильным числом и выбрать его
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)

    #нажимаем на кнопку submit
    browser.find_element_by_xpath("//*[@type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка

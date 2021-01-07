from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #считываем значение для переменной x
    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    
    #считаем значение f(x)
    y = calc(x)
    
    #вводим значение f(x) в поле
    text_form = browser.find_element_by_xpath("//*[@class='form-control']")
    text_form.send_keys(y)
    
    #отмечаем необходимые флажки и радио-кнопки
    cb1 = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    cb1.click()
    rb2 = browser.find_element_by_xpath("//*[@id='robotsRule']")
    rb2.click()

    #нажимаем кнопку submit
    submit = browser.find_element_by_xpath("//*[@type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка
    

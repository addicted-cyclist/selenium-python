from selenium import webdriver
import time
import math


try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение x 
    x = browser.find_element_by_xpath("//*[@id='input_value']").text
    
    # считаем f(x)
    y = str(math.log(abs(12*math.sin(int(x)))))

    # вписать значение функции в поле
    form = browser.find_element_by_xpath("//*[@id='answer']")
    form.send_keys(y)
    
    # checkbox "i'm the robot"
    chbox = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    chbox.click()
    
    # скролл страницы и клик radiobutton
    radiob = browser.find_element_by_xpath("//*[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiob)
    radiob.click()

    # submit click
    submit = browser.find_element_by_xpath("//*[@type='submit']")
    submit.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка


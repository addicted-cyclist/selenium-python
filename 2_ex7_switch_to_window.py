from selenium import webdriver
import math
import time 

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажимаем на кнопулю "хочу отправиться в путешествие"
    browser.find_element_by_xpath("//*[@type='submit']").click()
    
    # имя новооткрывшегося окна
    new_window = browser.window_handles[1]
    
    # переходим к новой вкладке 
    browser.switch_to.window(new_window)

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

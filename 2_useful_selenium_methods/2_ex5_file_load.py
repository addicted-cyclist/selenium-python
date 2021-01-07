from selenium import webdriver
import time
import os 


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    f1 = browser.find_element_by_xpath("//*[@name='firstname']")
    f1.send_keys("Додичи")
    

    f2 = browser.find_element_by_xpath("//*[@name='lastname']")
    f2.send_keys("Краморов")
    

    f3 = browser.find_element_by_xpath("//*[@name='email']")
    f3.send_keys("gmilo@gmilo.com")
    

    # в переменную current_dir сохраняем путь до текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя прикрепляемого файла
    file_path = os.path.join(current_dir, 'file.txt')

    # находим на странице элемент для добавления файла 
    load = browser.find_element_by_xpath("//*[@name='file']")
    load.send_keys(file_path)
    
    # кнопка submit
    submit = browser.find_element_by_xpath("//*[@type='submit']")
    submit.click()

    # принтуем
    print(os.path.abspath(__file__)) 
    print(os.path.abspath(os.path.dirname(__file__)))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка

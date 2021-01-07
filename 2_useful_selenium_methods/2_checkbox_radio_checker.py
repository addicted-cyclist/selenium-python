from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем дефолтную галку в checkbox "I'm the robot"
    cb1 = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    cb1_checked = cb1.get_attribute("checked")
    assert cb1_checked is None, "'I'm the robot' selected by default"

#проверяем дефолтную активность radiobutton "people rule"
    rb1 = browser.find_element_by_xpath("//*[@id='peopleRule']")
    rb1_checked = rb1.get_attribute("checked")
    assert rb1_checked is not None, "'people rule' is not selected by default"

#проверяем значение атрибута disabled у кнопки Submit
    rb2 = browser.find_element_by_xpath("//*[@id='robotsRule']")
    rb2_disabled = rb2.get_attribute("checked")
    assert rb2_disabled is None, "'robots rule' selected by default"


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)      
    browser.quit()

# не забываем оставить пустую строку в конце файла

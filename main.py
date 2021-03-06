from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time

def click_send():
    button2 = driver.find_elements_by_class_name('btn')[1]
    ActionChains(driver).move_to_element(button2).click(button2).perform()

def positive():
    rand = randint(0, 2)
    return rand

def negative():
    try:
        rand = randint(3,5)
        return rand
    except:
        rand = randint(2,3)
        return rand
    
    
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

while True:
    driver.get('https://www.survio.com/survey/d/X7W3M9I5F1Z3H7A9H')

    start_button = driver.find_element_by_xpath('//*[@id="survey"]/div/div[1]/div/div/div/div[2]/div/div/div[2]')
    start_button.click()


    #kazdy blok s otazkami - 8 dokopy
    answers = driver.find_elements_by_class_name('answers')

    i = 1


    negative_or_positive = randint(1, 2)
    if negative_or_positive == 1:
        print('positive answers')
    elif negative_or_positive == 2:
        print('negative answers')


    # kazdy blok osobitne od 1 po 8
    for answer in answers:
        print('question ' +str(i))
        i += 1
        driver.implicitly_wait(1)
        
        items = answer.find_elements_by_class_name('item')

        if negative_or_positive == 1:
            button = items[positive()]
            ActionChains(driver).move_to_element(button).click(button).perform()
            print(button.text)
        elif negative_or_positive == 2:
            button = items[negative()]
            ActionChains(driver).move_to_element(button).click(button).perform()
            print(button.text)


    click_send()
    time.sleep(2)
    driver.refresh()
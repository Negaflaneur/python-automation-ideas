from selenium import webdriver
import time
import pyinputplus as pyip

browser = webdriver.Chrome('PATH')

browser.get('URL')

try:
    email = browser.find_element_by_id('email')
    print(f'Found element with id {email.tag_name}')

    user_name = 'example@gmail.com'
    email.send_keys(user_name)
    email.submit()

    time.sleep(5)
    password_field = browser.find_element_by_id('password')
    password = pyip.inputPassword()
    password_field.send_keys(password)
    password_field.submit()
except:
    print("No elements found with this id")
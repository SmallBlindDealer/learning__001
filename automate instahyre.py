from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time


def retry_execute(func):
    def wrap(*args, **kwargs): 
        c = 3
        while c:
            try:
                func(*args, **kwargs)
                break
            except Exception as e:
                print(str(e))
            c-=1    
    return wrap 


@retry_execute
def execute_(driver, querySelector, value, isButton=False):
    _element = driver.find_element(By.CSS_SELECTOR, querySelector)
    if isButton:
        _element.click()
        return
    _element.clear()  
    _element.send_keys(value)


def login(driver, email_id, pass_):
    execute_(driver, "#email", email_id, isButton=False)
    execute_(driver, "#password", pass_, isButton=False)
    execute_(driver, "#login-form > button", None, isButton=True)


def run_apply(driver, apply_selector=None):
    c = 0
    while True:
        if not apply_selector:
            apply_selector = "#candidate-suggested-employers > div > div:nth-child(3) > div > div > div.application-modal-wrap > div.container > div.row.bar-actions.ng-scope > div.apply.ng-scope > button"
        execute_(driver, apply_selector, None, isButton=True)
        print(c)
        c+=1
        time.sleep(5)



driver = webdriver.Chrome()
time.sleep(1)

driver.get("https://www.instahyre.com/candidate/opportunities/")

time.sleep(3)
email_id = "shiv.s.keshari@gmail.com"
pass_ = "1qazXsw2@11"

login(driver, email_id, pass_)
driver.implicitly_wait(10)


# TODO: ->>---> select here save_job_search filter if not create pelase create
filter_ = "#search-j1"
execute_(driver, filter_, None, isButton=True)
execute_(driver, "#show-results", None, isButton=True)
execute_(driver, "#interested-btn", None, isButton=True)
run_apply(driver)

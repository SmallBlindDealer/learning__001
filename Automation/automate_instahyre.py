from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def retry_execute(func):
    def wrap(*args, **kwargs): 
        c = 3
        while c:
            try:
                func(*args, **kwargs)
                return True
            except NoSuchElementException:
                print("no such element!")
                return False
            except Exception as e:
                print(str(e))
            c-=1    
        return False
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
        res = execute_(driver, apply_selector, None, isButton=True)
        if not res:
            not_now = "#enable-whatsapp-modal > div > div > div.application-modal-wrap > div.application-modal-action.text-center.cancel-button > button"
            res = execute_(driver, not_now, None, isButton=True)
            if not res:
                apply = "body > div.application-modal.candidate-apply-all-modal.ng-scope > div > div.application-modal-wrap > div.content.text-center.top-margin > div > div.col-sm-4.col-xs-6.col-sm-offset-2 > button"
                execute_(driver, apply, None, isButton=True)
        
        print(c)
        c+=1
        time.sleep(5)





# chrome_options = Options()
# chrome_options.add_argument("--headless")
# # options.add_argument("--headless=new")
# # options.add_argument("window-size=1920,1080")
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()
time.sleep(1)


driver.get("https://www.instahyre.com/candidate/opportunities/")

time.sleep(3)
email_id = "shiv.s.keshari@gmail.com"
pass_ = "1qazXsw2@11"

login(driver, email_id, pass_)
driver.implicitly_wait(10)


execute_(driver, "#job-search-section > div.job-search-heading.ng-scope.cursor-pointer", None, isButton=True)

# TODO: ->>---> select here save_job_search filter if not create pelase create
filter_ = "#search-j1"
print("-1")
execute_(driver, filter_, None, isButton=True)
time.sleep(1)
print("-2")
execute_(driver, "#show-results", None, isButton=True)
time.sleep(1)
print("-3")
execute_(driver, "#interested-btn", None, isButton=True)
time.sleep(1)
print("-4")
run_apply(driver)
# 
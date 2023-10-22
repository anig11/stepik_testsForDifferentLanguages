from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button_add_to_basket = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        present_elem = True
    except:
        present_elem = False    
    assert present_elem, "Button not found" 
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    #Create odj to drive browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #open webpage 
    driver.get("https://github.com/login")

    #find element to input login
    login_elem = driver.find_element(By.ID, "login_field")

    #input non correct username
    login_elem.send_keys("sergiinuten@istalemail.com")

    #find element for password
    pass_elem = driver.find_element(By.ID, 'password')

    #input non coorrect pass
    pass_elem.send_keys("wrong_password")

    #find btn sign-in
    btn_elem = driver.find_element(By.NAME, "commit")

    #click btn
    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    time.sleep(3)


    #close browser
    driver.close()

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui_rztk
def test_search_result_for_ru_request():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://epicentrk.ua/")

    time.sleep(3)

    search_string = driver.find_element(By.CLASS_NAME, "_JcImSJ" )

    search_string.send_keys("Мебель")

    search_btn = driver.find_element(By.CLASS_NAME, "_cvO7u1")

    search_btn.click()

    time.sleep(3)
    
    catalog_heading_name = driver.find_element(By.CLASS_NAME, "shop-categories__title.nc").text

    assert catalog_heading_name == "Меблі"
    
    driver.close()

@pytest.mark.epic
def test_incorrect_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://epicentrk.ua/")

    Login_pic = driver.find_element(By.CLASS_NAME, "_VckGS5")

    Login_pic.click()

    time.sleep(2)

    login_elem = driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div[2]/div/div/div[1]/div[2]/div")

    login_elem.send_keys("991234567")

    password_elem = driver.find_element(By.CLASS_NAME, "epicentr-nuxt-components-ui-form-password__field__input")

    password_elem.send_keys("passworg")

    login_btn = driver.find_element(By.CLASS_NAME, "epicentr-nuxt-components-ui-button__button epicentr-nuxt-components-ui-button__button--blue epicentr-nuxt-components-forms-auth__send")

    login_btn.click()




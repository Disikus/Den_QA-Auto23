from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)
    
    def try_login(self, username, password):
        # Find element where we will input non correct login/pass
        login_elem = self.driver.find_element(By.ID, 'login_field')

        #input username
        login_elem.send_keys(username)

        #find elemnt for input password
        pass_elem = self.driver.find_element(By.ID, "password")

        #input pass

        pass_elem.send_keys(password)

        #find log in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        #click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
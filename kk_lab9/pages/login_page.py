from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.success_sign_locator = (By.XPATH, "/html/body/div[@class='content']/div[@class='container']/div[@class='row']/div[@class='col-md-12']/div[@class='alert alert-success']")
        self.login_field_locator = (By.XPATH, "//*[@name='login']")
        self.password_field_locator = (By.XPATH, "//*[@id='pasword']")
        self.login_button_locator = (By.XPATH, "//form[@id='login']/button[@class='btn btn-default']")

    def input_login(self, login):
        login_field = self.wait.until(EC.visibility_of_element_located(self.login_field_locator))
        login_field.clear()
        login_field.send_keys(login)

    def input_password(self, passwd):
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_field_locator))
        password_field.clear()
        password_field.send_keys(passwd)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button_locator))
        login_button.click()

    def get_success_sign_content(self):
        success_sign = self.wait.until(EC.visibility_of_element_located(self.success_sign_locator))
        return success_sign.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.order_button_locator = (By.XPATH, "/html/body/div[@class='content']/div[@class='prdt']/div[@class='container']/div[@class='prdt-top']/div[@class='col-md-12']/div[@class='product-one cart']/div[@class='col-md-6 account-left']/form/button[@class='btn btn-default']")

    def order_product(self):
        wait = WebDriverWait(self.driver, 5)
        order_button = wait.until(EC.element_to_be_clickable(self.order_button_locator))
        order_button.click()

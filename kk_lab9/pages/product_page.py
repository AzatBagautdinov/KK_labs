from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.color_menu_locator = (By.XPATH, "/html/body/div[@class='content']/div[@class='single contact']/div[@class='container']/div[@class='single-main']/div[@class='col-md-12 single-main-left']/div[@class='sngl-top']/div[@class='col-md-7 single-top-right']/div[@class='single-para simpleCart_shelfItem']/div[@class='available']/ul/li/select")
        self.product_price_field_locator = (By.XPATH, "//h5[@id='base-price']")
        self.product_title_field_locator = (By.XPATH, "/html/body/div[@class='content']/div[@class='single contact']/div[@class='container']/div[@class='single-main']/div[@class='col-md-12 single-main-left']/div[@class='sngl-top']/div[@class='col-md-7 single-top-right']/div[@class='single-para simpleCart_shelfItem']/h2")
        self.add_button_locator = (By.XPATH, "//a[@id='productAdd']")
        self.cart_button_locator = (By.XPATH, "/html/body/div[@class='top-header']/div[@class='container']/div[@class='top-header-main']/div[@class='col-md-6 top-header-left'][2]/div[@class='cart box_1']/a/div[@class='total']")
        self.product_title_in_cart_locator = (By.XPATH, "//div[@id='cart']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@class='modal-body']/div[@class='table-responsive']/table[@class='table table-hover table-striped']/tbody/tr[1]/td[2]/a")
        self.product_count_in_cart_locator = (By.XPATH, "//div[@id='cart']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@class='modal-body']/div[@class='table-responsive']/table[@class='table table-hover table-striped']/tbody/tr[1]/td[3]")
        self.product_price_in_cart_locator = (By.XPATH, "//div[@id='cart']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@class='modal-body']/div[@class='table-responsive']/table[@class='table table-hover table-striped']/tbody/tr[1]/td[4]")
        self.total_count_locator = (By.XPATH, "//div[@id='cart']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@class='modal-body']/div[@class='table-responsive']/table[@class='table table-hover table-striped']/tbody/tr[2]/td[@class='text-right cart-qty']")
        self.total_cost_locator = (By.XPATH, "//div[@id='cart']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@class='modal-body']/div[@class='table-responsive']/table[@class='table table-hover table-striped']/tbody/tr[3]/td[@class='text-right cart-sum']")
        self.order_button_locator = (By.XPATH, "//div[@id='cart']/div[@class='modal-dialog modal-lg']/div[@class='modal-content']/div[@class='modal-footer']/a[@class='btn btn-primary']")
        self.submit_order_button_locator = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div/div/div[3]/form/button")

        self.product_price = None
        self.product_title = None
        self.product_color = None

    def set_product_price(self):
        price_element = self.driver.find_element(*self.product_price_field_locator)
        self.product_price = price_element.text

    def get_product_price(self):
        return self.product_price

    def set_product_title(self):
        title_element = self.driver.find_element(*self.product_title_field_locator)
        self.product_title = f"{title_element.text} {self.product_color or ''}".strip()

    def get_product_title(self):
        return self.product_title

    def add_product_in_cart(self):
        self.driver.find_element(*self.add_button_locator).click()

    def choose_color(self, color):
        select_element = Select(self.driver.find_element(*self.color_menu_locator))
        select_element.select_by_visible_text(color)
        self.product_color = f"({color})"

    def get_product_price_in_cart(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(self.product_price_in_cart_locator))
        return self.driver.find_element(*self.product_price_in_cart_locator).text

    def get_product_title_in_cart(self):
        return self.driver.find_element(*self.product_title_in_cart_locator).text

    def get_product_count_in_cart(self):
        return self.driver.find_element(*self.product_count_in_cart_locator).text

    def get_total_count(self):
        return self.driver.find_element(*self.total_count_locator).text

    def get_total_cost(self):
        return self.driver.find_element(*self.total_cost_locator).text

    def order_product_from_cart(self):
        self.driver.find_element(*self.order_button_locator).click()

    def submit_order(self):
        wait = WebDriverWait(self.driver, 10)
        submit_button = wait.until(EC.element_to_be_clickable(self.submit_order_button_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
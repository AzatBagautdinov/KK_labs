from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.search_string = ""

    @property
    def search_bar(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='typeahead']")))

    @property
    def first_product_card(self):
        xpath = ("/html/body/div[@class='content']/div[@class='prdt']/div[@class='container']/div[@class='prdt-top']/div[@class='col-md-9 prdt-left']/div[@class='product-one']/div[@class='col-md-4 product-left p-left'][1]/div[@class='product-main simpleCart_shelfItem']")
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def input_search_bar(self, text: str):
        self.search_bar.clear()
        self.search_bar.send_keys(text)
        self.search_string = text

    def submit_search_bar(self):
        self.search_bar.submit()
        self.wait_for_first_product_card()

    def wait_for_first_product_card(self, timeout=10):
        xpath_title = ".//div[@class='product-bottom']/h3"
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.first_product_card.find_element(By.XPATH, xpath_title).text != ""
        )

    def first_product_card_title_contains_string(self) -> bool:
        title_element = self.first_product_card.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]/div/div[1]/div/div[1]/h3")
        title = title_element.text
        print(f"Title found: '{title}', searching for: '{self.search_string}'")
        return self.search_string.lower() in title.lower()

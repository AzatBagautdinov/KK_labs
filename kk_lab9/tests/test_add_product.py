import pytest
import yaml
from pages.product_page import ProductPage
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_add_product_in_cart(driver):
    with open("config/add_to_cart.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["product_page"])
    product_page = ProductPage(driver)

    product_page.choose_color(config["color"])
    product_page.set_product_price()
    product_page.set_product_title()
    product_page.add_product_in_cart()

    assert product_page.get_product_price_in_cart() == product_page.get_product_price()[1:]
    assert product_page.get_product_title_in_cart() == product_page.get_product_title()
    assert product_page.get_product_count_in_cart() == "1"
    assert product_page.get_total_count() == "1"
    assert product_page.get_total_cost() == product_page.get_product_price()

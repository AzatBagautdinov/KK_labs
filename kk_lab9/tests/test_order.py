import pytest
import yaml
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.order_page import OrderPage
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_order(driver):
    with open("config/order.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["login_page"])
    login_page = LoginPage(driver)
    login_page.input_login(config["login"])
    login_page.input_password(config["password"])
    login_page.click_login_button()

    assert login_page.get_success_sign_content() == "Вы успешно авторизованы"

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

    product_page.order_product_from_cart()

    order_page = OrderPage(driver)
    order_page.order_product()
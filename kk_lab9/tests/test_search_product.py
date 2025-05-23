import pytest
import yaml
from pages.main_page import MainPage
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search_product(driver):
    with open("config/product_search.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["main_page"])
    main_page = MainPage(driver)

    main_page.input_search_bar(config["search_string"])
    main_page.submit_search_bar()

    assert main_page.first_product_card_title_contains_string()

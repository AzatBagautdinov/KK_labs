import pytest
import yaml
from pages.login_page import LoginPage
from utils.driver_factory import get_driver  # предполагается, что этот метод у тебя уже есть

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()  # драйвер инициализируется там, где уже прописан путь или по PATH
    yield driver
    driver.quit()

def test_login(driver):
    with open("config/login.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["login_page"])

    login_page = LoginPage(driver)
    login_page.input_login(config["login"])
    login_page.input_password(config["password"])
    login_page.click_login_button()

    success_message = login_page.get_success_sign_content()
    assert success_message == "Вы успешно авторизованы"
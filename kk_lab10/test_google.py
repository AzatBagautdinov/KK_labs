import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.firefox.options import Options as FirefoxOpts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SITE_URL = "http://shop.qatl.ru"
MEN_CATEGORY_URL = "http://shop.qatl.ru/category/men"

@pytest.fixture(params=["chrome", "firefox"])
def browser_driver(request):
	browser_choice = request.param
	if browser_choice == "chrome":
		options = ChromeOpts()
	elif browser_choice == "firefox":
		options = FirefoxOpts()
	else:
		raise RuntimeError(f"Unsupported browser: {browser_choice}")
	
	sess = webdriver.Remote(
		command_executor="http://localhost:4444/wd/hub",
		options=options
	)
	yield sess
	sess.quit()


def test_open_men_section(browser_driver):
	browser_driver.get(SITE_URL)
	wait = WebDriverWait(browser_driver, 10)
	link_to_men = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Men")))
	link_to_men.click()
	wait.until(EC.url_to_be(MEN_CATEGORY_URL))

	assert browser_driver.current_url == MEN_CATEGORY_URL, \
		f"Unexpected URL: {browser_driver.current_url}"
	assert "Men" in browser_driver.title, \
		f"Unexpected title: {browser_driver.title}"
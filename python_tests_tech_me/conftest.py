import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pages.pages21vek


@pytest.fixture(scope='session', autouse=True)
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.delete_all_cookies()
    open_test_url = pages.pages21vek
    open_test_url.open_url_accept_cookie(driver)
    yield driver
    driver.close()


@pytest.fixture()
def driver_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.delete_all_cookies()
    open_test_url = pages.pages21vek
    open_test_url.open_url_accept_cookie(driver)
    yield driver
    driver.close()
    driver.quit()

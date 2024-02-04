import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_locator(driver_chrome):
    driver_chrome.get('https://www.bbc.com/news')

    try:
        WebDriverWait(driver_chrome, 4).until(EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'gs-c-promo') and contains(@data-entityid, 'container-top-stories#3')]")))
        # WebDriverWait(driver_chrome, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.orbit-header-more')))
        patch_add_user = "//div[contains(@class, 'gs-c-promo') and contains(@data-entityid, 'container-top-stories#3')]"
        driver_chrome.find_element(By.XPATH, patch_add_user).click()
        time.sleep(5)
        print(' локатор найден')


    except NoSuchElementException:
        print('не найден')
    except TimeoutException:
        print(' таймаут / не найден')
    except InvalidSelectorException:
        print('InvalidSelectorException')

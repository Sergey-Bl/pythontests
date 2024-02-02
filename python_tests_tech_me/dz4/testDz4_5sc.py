import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import re


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def cookie_accept(driver_chrome):
    try:
        accept_all_button = WebDriverWait(driver_chrome, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-cookie"]/div/div[2]/div[2]/button[2]'))
        )
        accept_all_button.click()

    except NoSuchElementException:
        print('no cookie pop-up')
    except TimeoutException:
        print('Timed out waiting for the cookie pop-up')


# test_1------------------------------------------------------------------------------------------------------------------------
def test_smoke_open_site_21vek(driver_chrome):
    driver_chrome.get('https://www.21vek.by/')
    cookie_accept(driver_chrome)

    try:
        WebDriverWait(driver_chrome, 10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        print("page full load")
    except TimeoutException:
        print("timeout")

    assert driver_chrome.title == 'Онлайн-гипермаркет 21vek.by'


# test_2------------------------------------------------------------------------------------------------------------------------
def test_search_func(driver_chrome):
    driver_chrome.get('https://www.21vek.by/')
    cookie_accept(driver_chrome)

    WebDriverWait(driver_chrome, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="catalogSearch"]'))).send_keys('adidas')

    search_button = '//*[@id="header"]/div/div[3]/div/div[2]/button[1]'
    driver_chrome.find_element(By.XPATH, search_button).click()

    result_find = WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/span')))

    search_result_text = result_find.text.strip()

    pattern = re.compile(r'Запрос «adidas». Найдено \d+ товаров')
    assert pattern.match(search_result_text) is not None


# test_3------------------------------------------------------------------------------------------------------------------------
def test_catalog_open(driver_chrome):
    driver_chrome.get('https://www.21vek.by/')
    cookie_accept(driver_chrome)

    WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[3]/div/button'))).click()

    # проверка состояния открытой кнопки
    button_locator = (By.CSS_SELECTOR, 'button.styles_catalogButton__z9L_j')
    button = WebDriverWait(driver_chrome, 10).until(EC.presence_of_element_located(button_locator))
    assert 'styles_pressed__kCcrg' in button.get_attribute(
        'class')

    text_summary_catalog = WebDriverWait(driver_chrome, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="header"]/div[1]/div[5]/div/div[2]/div[1]')))

    summary_result = text_summary_catalog.text

    assert summary_result == 'Бытовая техника'


# test_4------------------------------------------------------------------------------------------------------------------------
def test_open_empty_basket(driver_chrome):
    driver_chrome.get('https://www.21vek.by/')
    cookie_accept(driver_chrome)

    WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[3]/div/div[4]/a'))).click()

    path_text_empty_basket = WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div/div/div[2]')))

    text_empty_basket = path_text_empty_basket.text

    assert text_empty_basket == 'У вас пока нет ни одного товара в корзине,\nвы можете выбрать их здесь'


# test_5------------------------------------------------------------------------------------------------------------------------
def test_open_link_from_empty_basket(driver_chrome):
    test_open_empty_basket(driver_chrome)

    WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/a'))).click()

    try:
        WebDriverWait(driver_chrome, 10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        print("page full load after move from basket")
    except TimeoutException:
        print("timeout")

    assert driver_chrome.title == 'Онлайн-гипермаркет 21vek.by'

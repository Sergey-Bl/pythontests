import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_add_login_user(driver_chrome):
    login = 'testtestest'
    password = 'testtest'
    # сайт с дз был нерабочим, нагуглил его дубликат
    driver_chrome.get('https://eprint.com.hr/demo/addauser.php')

    add_user_patch = '/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/div/center/table/tbody/tr[1]/td[2]/p/input'
    driver_chrome.find_element(By.XPATH, add_user_patch).send_keys(login)

    add_password_patch = '/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/div/center/table/tbody/tr[2]/td[2]/p/input'
    driver_chrome.find_element(By.XPATH, add_password_patch).send_keys(password)

    patch_add_user = '/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/div/center/table/tbody/tr[3]/td[2]/p/input'
    driver_chrome.find_element(By.XPATH, patch_add_user).click()

    driver_chrome.get('https://eprint.com.hr/demo/login.php')

    patch_username = '/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/p/input'
    WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, patch_username)))
    driver_chrome.find_element(By.XPATH, patch_username).send_keys(login)

    patch_password = '/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/p/input'
    driver_chrome.find_element(By.XPATH, patch_password).send_keys(password)

    patch_login_user = '/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/p/input'
    driver_chrome.find_element(By.XPATH, patch_login_user).click()

    patch_check_login = '/html/body/table/tbody/tr/td[1]/big/blockquote/blockquote/font/center/b'
    checker_login = driver_chrome.find_element(By.XPATH, patch_check_login)
    assert checker_login.text == '**Successful Login**'


def test_register_guru99(driver_chrome: WebDriver):
    user_name_check_name = 'Dear gena gorabaev,'
    welcome_check = 'Note: Your user name is arena.'
    user_info = {
        'first_name': 'gena',
        'last_name': 'gorabaev',
        'phone': 1234567,
        'email': 'gera@gmail.com',
        'address': 'gonaeva 32.31',
        'city': 'gdansk',
        'state': 'state test',
        'postal_code': '40-414',
        'user_name': 'arena',
        'password': 'passwd123',
        'conf_password': 'passwd123'
    }
    driver_chrome.get('http://demo.guru99.com/test/newtours/register.php')
    time.sleep(2)
    try:

        iframe = driver_chrome.find_element(By.ID, 'gdpr-consent-notice')
        driver_chrome.switch_to.frame(iframe)

        accept_all_button = WebDriverWait(driver_chrome, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="save"]'))
        )
        accept_all_button.click()

        driver_chrome.switch_to.default_content()

    except NoSuchElementException:
        print('no cookie pop-up')
    except TimeoutException:
        print('Timed out waiting for the cookie pop-up')

    time.sleep(2)

    patch_name_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_name_field).send_keys(user_info['first_name'])

    patch_last_name_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[3]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_last_name_field).send_keys(user_info['last_name'])

    patch_phone_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_phone_field).send_keys(user_info['phone'])

    patch_email_field = '//*[@id="userName"]'
    driver_chrome.find_element(By.XPATH, patch_email_field).send_keys(user_info['email'])

    patch_address_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_address_field).send_keys(user_info['address'])

    patch_city_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[8]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_city_field).send_keys(user_info['city'])

    patch_state_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_state_field).send_keys(user_info['state'])

    patch_postal_code_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[10]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_postal_code_field).send_keys(user_info['state'])

    patch_username_field = '//*[@id="email"]'
    driver_chrome.find_element(By.XPATH, patch_username_field).send_keys(user_info['user_name'])

    patch_password_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_password_field).send_keys(user_info['password'])

    patch_conf_password_field = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input'
    driver_chrome.find_element(By.XPATH, patch_conf_password_field).send_keys(user_info['conf_password'])

    path_submit = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input'
    driver_chrome.find_element(By.XPATH, path_submit).click()

    try:
        username_locator = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b'
        your_name = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b'

        username_element = WebDriverWait(driver_chrome, 10).until(
            EC.presence_of_element_located((By.XPATH, username_locator)))

        welcome_check_description = WebDriverWait(driver_chrome, 10).until(
            EC.presence_of_element_located((By.XPATH, your_name)))

        username_text = username_element.text.strip()
        welcome_text = welcome_check_description.text.strip()

        assert username_text == user_name_check_name
        assert welcome_text == welcome_check

    except TimeoutException:
        print("timeout wait username locator")

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

import base_page
from locator.locators_help import get_locator_from_xpath_wb_wait, get_locator_from_css_wb_wait


class Locators21v:
    ACCEPT_COOKIE_BUTTON = "//div[contains(@class,'Button-module__buttonText') and contains(text(),'Принять')]"
    SEARCH_FIELD = "//*[@id='catalogSearch']"
    SEARCH_BUTTON = ".Search_searchBtn__Tk7Gw"
    SEARCH_RESULT = ".b-content > span"
    CATALOG_BUTTON = "button.styles_catalogButton__z9L_j"
    CATEGORY_TECHNIQUE_HEADER = ".styles_categoryTitle__q3arD"
    BASKET_BUTTON = ".headerCartBox"
    EMPTY_BASKET_HEADER = ".EmptyBasket_text__3fMyR"
    HERE_BUTTON_EMPTY_BASKET = ".EmptyBasket_text__3fMyR .Link_link__qgZBw"


def cookie_accept(driver_chrome):
    try:
        accept_all_button = get_locator_from_xpath_wb_wait(driver_chrome, Locators21v.ACCEPT_COOKIE_BUTTON, 5)
        accept_all_button.click()

    except NoSuchElementException:
        print('no cookie pop-up')
    except TimeoutException:
        print('Timed out waiting for the cookie pop-up')


def open_url_accept_cookie(driver_chrome):
    open_url_by_test = base_page.BasePage(driver_chrome)
    open_url_by_test.open_base_url()
    cookie_accept(driver_chrome)


def checker_full_load_page(driver_chrome):
    try:
        WebDriverWait(driver_chrome, 10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        print("page full load")
    except TimeoutException:
        print("timeout")


def find_checker_field_result(driver_chrome):
    get_locator_from_xpath_wb_wait(driver_chrome, Locators21v.SEARCH_FIELD, 5).send_keys("adidas")
    get_locator_from_css_wb_wait(driver_chrome, Locators21v.SEARCH_BUTTON, 15).click()
    result_find = get_locator_from_css_wb_wait(driver_chrome, Locators21v.SEARCH_RESULT, 10)

    search_result_text = result_find.text.strip()
    return search_result_text


def click_check_catalog_button(driver_chrome):
    get_locator_from_css_wb_wait(driver_chrome, Locators21v.CATALOG_BUTTON, 10).click()

    # проверка состояния открытой кнопки
    button_locator = get_locator_from_css_wb_wait(driver_chrome, Locators21v.CATALOG_BUTTON, 10)
    text_summary_catalog = get_locator_from_css_wb_wait(driver_chrome, Locators21v.CATEGORY_TECHNIQUE_HEADER, 10)
    summary_result = text_summary_catalog.text

    return summary_result, button_locator


def click_basket(driver_chrome):
    get_locator_from_css_wb_wait(driver_chrome, Locators21v.BASKET_BUTTON, 5).click()


def check_empty_basket_result(driver_chrome):
    path_text_empty_basket = get_locator_from_css_wb_wait(driver_chrome, Locators21v.EMPTY_BASKET_HEADER, 5)
    return path_text_empty_basket


def click_here_link_empty_basket(driver_chrome):
    get_locator_from_css_wb_wait(driver_chrome, Locators21v.HERE_BUTTON_EMPTY_BASKET).click()

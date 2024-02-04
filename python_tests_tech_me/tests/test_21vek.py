import pytest
import re

import pages.pages21vek
from conftest import driver_chrome


@pytest.mark.smoke("test-001")
def test_smoke_open_site_21vek(driver_chrome):
    open_test_url = pages.pages21vek
    open_test_url.open_url_accept_cookie(driver_chrome)
    open_test_url.checker_full_load_page(driver_chrome)
    assert driver_chrome.title == 'Онлайн-гипермаркет 21vek.by'


@pytest.mark.search("test-002")
def test_search_func(driver_chrome):
    open_test_url_find_test = pages.pages21vek
    open_test_url_find_test.open_url_accept_cookie(driver_chrome)
    search_result_text = open_test_url_find_test.find_checker_field_result(driver_chrome)
    pattern = re.compile(r'Запрос «adidas». Найдено? \d+ товар(?:ов)?')
    assert pattern.match(search_result_text) is not None


@pytest.mark.basket("test-003")
def test_catalog_open(driver_chrome):
    open_test_url = pages.pages21vek
    open_test_url.open_url_accept_cookie(driver_chrome)
    summary_result, button_locator = pages.pages21vek.click_check_catalog_button(driver_chrome)
    assert 'styles_pressed__kCcrg' in button_locator.get_attribute('class')
    assert summary_result == 'Бытовая техника'


@pytest.mark.basket("test-004")
def test_open_empty_basket(driver_chrome):
    open_test_url = pages.pages21vek
    open_test_url.open_url_accept_cookie(driver_chrome)
    pages.pages21vek.click_basket(driver_chrome)
    path_text_empty_basket = pages.pages21vek.check_empty_basket_result(driver_chrome)
    text_empty_basket = path_text_empty_basket.text
    assert text_empty_basket == 'У вас пока нет ни одного товара в корзине,\nвы можете выбрать их здесь'


@pytest.mark.basket("test-005")
def test_open_link_from_empty_basket(driver_chrome):
    test_open_empty_basket(driver_chrome)
    pages.pages21vek.click_here_link_empty_basket(driver_chrome)
    pages.pages21vek.checker_full_load_page(driver_chrome)
    assert driver_chrome.title == 'Онлайн-гипермаркет 21vek.by'

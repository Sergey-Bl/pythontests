import pytest
import re
import pages.pages21vek


@pytest.mark.smoke("test-001")
def test_smoke_open_site_21vek(driver_chrome, driver_firefox):
    pages.pages21vek.checker_full_load_page(driver_chrome)
    assert driver_chrome.title == 'Онлайн-гипермаркет 21vek.by'


@pytest.mark.search("test-002")
@pytest.mark.parametrize("search_query", ["adidas", "nike", "iphone"])
def test_search_func(driver, search_query):
    search_result_text = pages.pages21vek.find_checker_field_result(driver, search_query)
    pattern = re.compile(rf'Запрос «{search_query}». Найдено? \d+ товар(?:ов)?')
    assert pattern.match(search_result_text) is not None


@pytest.mark.basket("test-003")
def test_catalog_open(driver_chrome):
    summary_result, button_locator = pages.pages21vek.click_check_catalog_button(driver_chrome)
    assert 'styles_pressed__kCcrg' in button_locator.get_attribute('class')
    assert summary_result == 'Бытовая техника'


@pytest.mark.basket("test-004")
def test_open_empty_basket(driver_chrome):
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

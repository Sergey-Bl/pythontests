import pytest
import data
import helpers.base_page_help
import pages.herokuapp_page


@pytest.mark.DZ8('TEST_CLICK(1)')
def test_click_simple(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.JS_CLICK_CHECK)
    hero_page.open_ht_url()
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).click_on(
        pages.herokuapp_page.HerokuAppLocators.HOME_BUTTON)
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_title(
        'The Internet')


@pytest.mark.DZ8('TEST_CLICK_JS(2)')
def test_click_js(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.JS_CLICK_CHECK)
    hero_page.open_ht_url()
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).force_click(
        pages.herokuapp_page.HerokuAppLocators.HOME_BUTTON)

    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_title(
        'The Internet')


@pytest.mark.DZ8('TEST_CLICK_MOUSE(3)')
def test_click_mouse(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.JS_CLICK_CHECK)
    hero_page.open_ht_url()
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).click_mouse(
        pages.herokuapp_page.HerokuAppLocators.HOME_BUTTON)

    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_title(
        'The Internet')


@pytest.mark.DZ8('TEST_CLICK_KEYBOARD(4)')
def test_click_keyboard(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.JS_CLICK_CHECK)
    hero_page.open_ht_url()
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).click_with_keyboard(
        pages.herokuapp_page.HerokuAppLocators.HOME_BUTTON)

    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_title(
        'The Internet')


@pytest.mark.DZ8('TEST_SEND_KEY(5)')
def test_send_key(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_SEND_KEYS)
    hero_page.open_ht_url()
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).send_symbols(
        pages.herokuapp_page.HerokuAppLocators.INPUT_FIELD, '12345')
    field_check = pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).get_value(
        pages.herokuapp_page.HerokuAppLocators.INPUT_FIELD)
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(field_check, '12345')


@pytest.mark.DZ8('TEST_CLEAR_KEY(6)')
def test_clear_key(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_SEND_KEYS)
    hero_page.open_ht_url()
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).send_symbols(
        pages.herokuapp_page.HerokuAppLocators.INPUT_FIELD, '12345')
    field_enter = pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).get_value(
        pages.herokuapp_page.HerokuAppLocators.INPUT_FIELD)
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(field_enter,
                                                                                      "12345")
    pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).clear_symbols(
        pages.herokuapp_page.HerokuAppLocators.INPUT_FIELD)
    field_check = pages.herokuapp_page.HelperTests(driver_chrome_heroku_test).get_value(
        pages.herokuapp_page.HerokuAppLocators.INPUT_FIELD)
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(field_check,
                                                                                      "")


@pytest.mark.DZ8("TEST_ALERT(7)")
def test_alert_accept(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_ALERTS)
    hero_page.open_ht_url()
    hero_page.locators_help.click_mouse(pages.herokuapp_page.HerokuAppLocators.BUTTON_CALL_ALERT)
    hero_page.alert_accept()
    result_check = hero_page.check_result_alert_tap()
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(
        "You successfully clicked an alert", result_check.text)


@pytest.mark.DZ8("TEST_ALERT_CANSEL(8)")
def test_cansel_alert(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_ALERTS)
    hero_page.open_ht_url()
    hero_page.locators_help.click_mouse(pages.herokuapp_page.HerokuAppLocators.BUTTON_CALL_JS_CONFIRM)
    hero_page.alert_cansel()
    result_check = hero_page.check_result_alert_tap()
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(
        "You clicked: Cancel", result_check.text)


@pytest.mark.DZ8("TEST_ALERT_ACCEPT_SEND_KEY(9)")
def test_cansel_alert_send_key(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_ALERTS)
    hero_page.open_ht_url()
    hero_page.locators_help.click_mouse(pages.herokuapp_page.HerokuAppLocators.BUTTON_CALL_JS_PROMPT)
    hero_page.alert_accept_send_keys()
    result_check = hero_page.check_result_alert_tap()
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(
        "You entered: test", result_check.text)


@pytest.mark.DZ8("TEST_BROWSER_TABS(10)")
def test_move_tabs(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_SEND_KEYS)
    hero_page.open_ht_url()
    hero_page.locators_help.click_mouse(pages.herokuapp_page.HerokuAppLocators.FOOTER_LINK)
    hero_page.move_main_tab()
    titles = hero_page.get_titles_of_tabs()

    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(
        "The Internet", titles[0])
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(
        "Home | Elemental Selenium", titles[1])


@pytest.mark.DZ8("TEST_IFRAME_MOVE(11)")
def test_iframe(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_IFRAME)
    hero_page.open_ht_url()
    hero_page.switch_to_iframe()
    elements_in_iframe = hero_page.find_elements_inside_iframe()
    text_in_iframe = None
    for element in elements_in_iframe:
        text_in_iframe = element.text
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(
        "Your content goes here.", text_in_iframe)


@pytest.mark.DZ8("TEST_UPLOAD(12)")
def test_upload(driver_chrome_heroku_test):
    hero_page = pages.herokuapp_page.HerokuAppPage(driver_chrome_heroku_test, data.HP_UPLOAD)
    hero_page.open_ht_url()
    hero_page.upload_file()
    check_uploaded = hero_page.check_text_uploaded_file()
    helpers.base_page_help.HelperTests(driver_chrome_heroku_test).assert_element_text(check_uploaded,
                                                                                      'File Uploaded!')

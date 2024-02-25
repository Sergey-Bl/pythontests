import helpers.base_page_help
import os
from pages.__init__ import BasePage, HelperTests, Alert


class HerokuAppLocators:
    HOME_BUTTON = "//*[@id='content']//a[text()='Home']"
    INPUT_FIELD = "//*[@type='number']"
    BUTTON_CALL_ALERT = "//*[@onclick ='jsAlert()']"
    BUTTON_CALL_JS_CONFIRM = "//*[@onclick ='jsConfirm()']"
    BUTTON_CALL_JS_PROMPT = "//*[@onclick ='jsPrompt()']"
    RESULT_ALERT = "//*[@id ='result']"
    FOOTER_LINK = "//*[@href='http://elementalselenium.com/']"
    IFRAME = "//iframe"
    INSIDE_IFRAME = "//*[@id='tinymce']"
    FILE_UPLOAD_BUTTON = "//*[@id='file-upload']"
    FILE_SUBMIT = "//*[@id='file-submit']"
    TITLE_FILE_UPLOADED = "//*[@class='row']//h3"


class HerokuAppPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.locators_help = HelperTests(driver)

    def open_ht_url(self):
        return self.driver.get(self.base_url)

    def alert_accept(self):
        alert = Alert(self.driver)
        alert.accept()

    def alert_cansel(self):
        alert = Alert(self.driver)
        alert.dismiss()

    def alert_accept_send_keys(self):
        alert = Alert(self.driver)
        alert.send_keys('test')
        alert.accept()

    def check_result_alert_tap(self):
        result_alert_page = HelperTests.get_locator_from_xpath_wb_wait(self.driver,
                                                                       HerokuAppLocators.RESULT_ALERT)
        return result_alert_page

    def move_main_tab(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[0])

    def get_titles_of_tabs(self):
        all_windows = self.driver.window_handles
        titles = []

        for window_handle in all_windows:
            self.driver.switch_to.window(window_handle)
            titles.append(self.driver.title)
        return titles

    def switch_to_iframe(self):
        iframe_element = helpers.base_page_help.HelperTests.get_locator_from_xpath_wb_wait(self.driver,
                                                                                           HerokuAppLocators.IFRAME)
        self.driver.switch_to.frame(iframe_element)

    def find_elements_inside_iframe(self):
        find_symbols = helpers.base_page_help.HelperTests(self.driver).get_locator_from_xpath_elements(
            HerokuAppLocators.INSIDE_IFRAME
        )
        return find_symbols

    def upload_file(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files', 'img.png'))

        helpers.base_page_help.HelperTests(self.driver).get_locator_from_xpath(
            HerokuAppLocators.FILE_UPLOAD_BUTTON).send_keys(file_path)

        helpers.base_page_help.HelperTests(self.driver).click_on(HerokuAppLocators.FILE_SUBMIT)

    def check_text_uploaded_file(self):
        ok_message_file_uploaded = helpers.base_page_help.HelperTests(self.driver).get_locator_from_xpath(
            HerokuAppLocators.TITLE_FILE_UPLOADED)
        return ok_message_file_uploaded.text

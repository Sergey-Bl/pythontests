from pages import main_page
from pages.__init__ import BasePage, get_locator_from_css_wb_wait


class SearchLocators:
    SEARCH_RESULT = ".b-content > span"
    PRODUCT_FROM_FIND_RANDOM = ".mindbox-pr-view.result__link"
    SEARCH_X_BUTTON = "Search_clearBtn__j9c8N"


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_product_from_find(self):
        get_locator_from_css_wb_wait(self.driver, SearchLocators.PRODUCT_FROM_FIND_RANDOM, 10).click()

    def cansel_selected_item_search(self):
        get_locator_from_css_wb_wait(self.driver, SearchLocators.SEARCH_X_BUTTON, 10).click()

    def find_and_select_product(self):
        main_page.MainPage(self.driver).find_checker_field_result()
        SearchPage(self.driver).click_product_from_find()

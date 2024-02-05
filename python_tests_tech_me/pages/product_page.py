from pages.__init__ import get_locator_from_css_wb_wait, get_locator_from_xpath_wb_wait, BasePage


class ProductLocators:
    PRODUCT_ADD_BASKET = ".item__buybtn"
    ADD_BASKET_BUTTON_AFTER_CLICK = ".j-button-clicked"
    COMPARE_LINK_ADD_RM = ".compare__link.g-pseudo_href"
    CAMPARE_LINK_PRODUCT_ADDED = ".compare__link.cr-compare__result"
    CAMPARE_COUNTER = ".g-counter.j-compare_counter"
    ADD_TO_FAVORITE = ".putaside__link.j-putaside"
    OPINION_LINK = "#j-tab_activate-review"
    ADD_OPINION_BUTTON = "#j-reviews__addlink button"
    OPINION_NAME_FILD = "//*[@class='g-form__text' and @name='data[Review][reviewer_name]']"
    OPINION_NUMBER_FIELD = "//*[@class='g-form__text' and @name='data[Review][reviewer_phone]']"
    OPINION_DESCRIPTION = "//*[@class='g-form__textarea' and @name='data[Review][review_text]']"
    OPINION_STARS = ".g-form__label.j-check.cr-check-required.cr-form__label-stars"
    OPINION_SENT = ".g-button.j-submit"
    IMAGE = ".l-photo"
    CLOSE_IMAGE_BUTTON = ".ui-icon-closethick"
    IMAGE_PANEL = ".ui-widget-content.ui-corner-all"


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_basket(self):
        get_locator_from_css_wb_wait(self.driver, ProductLocators.PRODUCT_ADD_BASKET, 5).click()

    def check_after_added_product(self):
        element_product_basket_check = get_locator_from_css_wb_wait(self.driver,
                                                                    ProductLocators.ADD_BASKET_BUTTON_AFTER_CLICK, 5)
        return element_product_basket_check

    def click_campare_link_add_remove(self):
        campare_link = get_locator_from_css_wb_wait(self.driver, ProductLocators.COMPARE_LINK_ADD_RM)
        campare_link.click()

    def campare_added_products_check(self):
        check_available_campare = get_locator_from_css_wb_wait(self.driver, ProductLocators.CAMPARE_LINK_PRODUCT_ADDED,
                                                               5)
        check_counter_campare = get_locator_from_css_wb_wait(self.driver, ProductLocators.CAMPARE_COUNTER, 5)
        return check_available_campare, check_counter_campare

    def favorite_link_click(self):
        get_locator_from_css_wb_wait(self.driver, ProductLocators.ADD_TO_FAVORITE, 10).click()
        favorite_element = get_locator_from_css_wb_wait(self.driver, ProductLocators.ADD_TO_FAVORITE, 10)
        return favorite_element

    def opinion_link_click(self):
        get_locator_from_css_wb_wait(self.driver, ProductLocators.OPINION_LINK, 5).click()

    def add_opinion_click(self):
        get_locator_from_css_wb_wait(self.driver, ProductLocators.ADD_OPINION_BUTTON, 5).click()

    def check_fields_opinion(self):
        name_opinion = get_locator_from_xpath_wb_wait(self.driver, ProductLocators.OPINION_NAME_FILD, 3).is_displayed()
        description_opinion = get_locator_from_xpath_wb_wait(self.driver, ProductLocators.OPINION_DESCRIPTION,
                                                             3).is_displayed()
        phone_opinion = get_locator_from_xpath_wb_wait(self.driver, ProductLocators.OPINION_NUMBER_FIELD,
                                                       3).is_displayed()
        sent_button_opinion = get_locator_from_css_wb_wait(self.driver, ProductLocators.OPINION_SENT, 3).is_displayed()
        return name_opinion, description_opinion, phone_opinion, sent_button_opinion

    def click_image_product(self):
        get_locator_from_css_wb_wait(self.driver, ProductLocators.IMAGE).click()

    def check_image_panel(self):
        x_image_button = get_locator_from_css_wb_wait(self.driver, ProductLocators.CLOSE_IMAGE_BUTTON).is_displayed()
        image_panel = get_locator_from_css_wb_wait(self.driver, ProductLocators.IMAGE_PANEL).is_displayed()
        return x_image_button, image_panel

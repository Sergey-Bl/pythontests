from pages.__init__ import BasePage, get_locator_from_css_wb_wait


class BasketPageLocators:
    BASKET_BUTTON = ".headerCartBox"
    EMPTY_BASKET_HEADER = ".EmptyBasket_text__3fMyR"
    HERE_BUTTON_EMPTY_BASKET = ".EmptyBasket_text__3fMyR .Link_link__qgZBw"


class BasketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_basket(self):
        get_locator_from_css_wb_wait(self.driver, BasketPageLocators.BASKET_BUTTON, 5).click()

    def check_empty_basket_result(self):
        path_text_empty_basket = get_locator_from_css_wb_wait(self.driver, BasketPageLocators.EMPTY_BASKET_HEADER, 5)
        return path_text_empty_basket

    def click_here_link_empty_basket(self):
        get_locator_from_css_wb_wait(self.driver, BasketPageLocators.HERE_BUTTON_EMPTY_BASKET).click()

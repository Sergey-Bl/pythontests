from locators.__init__ import By, EC, WebDriverWait


# ---------------------------------------------------------------
# CSS

def get_from_css(selector):
    return f'[class="{selector}"]'


def get_locator_from_class_css(driver, selector):
    selector = get_from_css(selector)
    return driver.find_element(By.CSS_SELECTOR, selector)


def get_locator_from_css(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


def get_locator_from_css_wb_wait(driver, selector, timeout=5):
    css = selector
    locator = (By.CSS_SELECTOR, css)

    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


# ---------------------------------------------------------------
# XPath

def get_from_xpath(selector):
    return f'//*[contains(@class, "{selector}")]'


def get_locator_from_class_xpath(driver, selector):
    selector = get_from_xpath(selector)
    return driver.find_element(By.XPATH, selector)


def get_locator_from_xpath(driver, selector):
    return driver.find_element(By.XPATH, selector)


def get_from_data_id_xpath(data_id):
    return f'//*[data-id="{data_id}"]'


def get_locator_from_xpath_wb_wait(driver, selector, timeout=5):
    xpath = selector
    locator = (By.XPATH, xpath)

    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

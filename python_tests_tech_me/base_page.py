class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.21vek.by/'

    def open_base_url(self):
        return self.driver.get(self.base_url)

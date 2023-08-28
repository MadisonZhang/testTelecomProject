from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def navigate_to(self,url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self,interval,locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
                ec.presence_of_element_located(locator_type_and_locator_tuple))

    def explicitly_wait_alert(self,interval):
        return WebDriverWait(self.driver, interval).until(ec.alert_is_present())

    def click_accept_alert(self):
        self.driver.switch_to.alert.accept()

    def clear_input(self):
        self.driver.clear()
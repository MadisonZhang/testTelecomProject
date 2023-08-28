
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# BasePage:
def explicitly_wait_and_find_link(self, interval, locator_type_and_locator_tuple):
    try:
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))
    except TimeoutException:
        self.driver.refresh()
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))
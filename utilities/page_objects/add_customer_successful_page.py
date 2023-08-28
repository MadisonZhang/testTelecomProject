from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.constants import MAX_WAIT_INTERVAL


class AddCustomerSuccessfulPage(BasePage):
    CUSTOMER_ID = (By.XPATH, "//div/table/tbody/tr[1]/td[2]/h3")
    PROMPT_MSG = (By.XPATH, "//div/table/tbody/tr[2]/td/b")
    HOME_LINK = (By.XPATH,"//*[@id='main']/div/div/ul/li/a")

    def get_customer_id(self):
        customer_id = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CUSTOMER_ID).text
        return customer_id

    def get_customer_added_msg(self):
        msg = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.PROMPT_MSG).text
        return msg

    def click_navigate_to_home_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HOME_LINK).click()

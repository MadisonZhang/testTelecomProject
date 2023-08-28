from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.constants import MAX_WAIT_INTERVAL

class CustomerLookUp(BasePage):
    ENTER_CUSTOMER_ID = (By.XPATH, "//input[@id='customer_id']")
    WARNING_MSG = (By.XPATH, "//label[@id='message2']")
    SUBMIT_BUTTON = (By.NAME, "submit")
    BACKGROUND_LABEL = (By.XPATH,"//section[@id='main']/div/form/div/div[2]/h3")
    CORRECT_CUSTOMER_ID_ALERT = (By.XPATH, "//section[@id='main']/div/h4")

    def fill_customer_id(self, customer_id):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ENTER_CUSTOMER_ID).send_keys(customer_id)

    def click_background(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.BACKGROUND_LABEL).click()

    def click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SUBMIT_BUTTON).click()

    def get_warning_msg(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.WARNING_MSG).text

    def invalid_customer_id_alert(self):
        return self.explicitly_wait_alert(MAX_WAIT_INTERVAL).text

    def alert_to_input_correct_id(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CORRECT_CUSTOMER_ID_ALERT).text

    def clear_customer_id_field(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ENTER_CUSTOMER_ID).clear()


from utilities.constants import MAX_WAIT_INTERVAL
from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class AddCustomerPage(BasePage):
    BACKGROUND_CHECK_DONE = (By.XPATH,"//div/label[@for='done']")
    BACKGROUND_CHECK_PENDING = (By.XPATH, "//div/label[@for='pending']")
    FIRST_NAME = (By.ID, "fname") # only letters input allowed
    LAST_NAME = (By.ID, "lname") # only letters input allowed
    EMAIL = (By.ID, "email") # email validation is on
    ADDRESS = (By.XPATH, "//textarea[@name='addr']") # special character not allowed
    TEL_NUMBER = (By.ID, "telephoneno") # only numbers are allowed
    SUBMIT_BUTTON = (By.NAME, "submit")
    RESET_BUTTON = (By.XPATH, "//li[@input='reset'")

    def click_background_done(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.BACKGROUND_CHECK_DONE).click()

    def click_background_pending(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.BACKGROUND_CHECK_PENDING).click()

    def fill_customer_first_name(self, first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.FIRST_NAME).send_keys(first_name)

    def fill_customer_last_name(self, last_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LAST_NAME).send_keys(last_name)

    def fill_customer_email(self, email):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMAIL).send_keys(email)

    def fill_customer_address(self, address):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADDRESS).send_keys(address)

    def fill_customer_tel_number(self, tel_number):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEL_NUMBER).send_keys(tel_number)

    def click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SUBMIT_BUTTON).click()

    def click_reset_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.RESET_BUTTON).click()
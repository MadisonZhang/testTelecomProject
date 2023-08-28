from utilities.constants import MAX_WAIT_INTERVAL
from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class IndexPage(BasePage):
    ADD_CUSTOMER = (By.PARTIAL_LINK_TEXT,"Add Customer")
    ADD_TARIFF_PLAN = (By.XPATH, "//div[@class='flex-item right']/div[1]/h3/a")
    ADD_TARIFF_PLAN_TO_CUSTOMER = (By.XPATH,"//div[@class='flex-item left']/div[2]/h3/a")
    PAY_BILLING = (By.PARTIAL_LINK_TEXT,"Pay Billing")

    def wait_and_click_add_customer_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADD_CUSTOMER).click()

    def wait_and_click_add_plan_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADD_TARIFF_PLAN).click()

    def wait_and_click_add_plan_to_customer(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADD_TARIFF_PLAN_TO_CUSTOMER).click()

    def wait_and_click_billing(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.PAY_BILLING).click()


from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.constants import MAX_WAIT_INTERVAL

class PayBilling(BasePage):
    CUSTOMER_INFO = (By.XPATH, "//section[@id='main']/div/h3")
    LOCAL_MIN_CHARGES = (By.XPATH, "//section[@id='main']/div/div/table/tbody/tr[1]/td[5]/b")
    INT_MIN_CHARGES = (By.XPATH, "//section[@id='main']/div/div/table/tbody/tr[2]/td[5]/b")
    SMS_CHARGES = (By.XPATH, "//section[@id='main']/div/div/table/tbody/tr[3]/td[5]/b")
    MONTHLY_RENTAL = (By.XPATH, "//section[@id='main']/div/div/table/tbody/tr[4]/td[2]/b")
    USAGE_CHARGES = (By.XPATH, "//section[@id='main']/div/div/table/tbody/tr[5]/td[2]/b")
    TOTAL_BILLING = (By.XPATH, "//section[@id='main']/div/div/table/tbody/tr[6]/td[2]/b")

    def get_customer_info(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CUSTOMER_INFO).text

    def get_local_min_charges(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LOCAL_MIN_CHARGES).text

    def get_int_min_charges(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.INT_MIN_CHARGES).text

    def get_sms_charges(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SMS_CHARGES).text

    def get_monthly_rental(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.MONTHLY_RENTAL).text

    def get_usage_charges(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USAGE_CHARGES).text

    def get_total_billing(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TOTAL_BILLING).text

    def get_local_min_charges(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LOCAL_MIN_CHARGES).text

    def get_local_min_charges(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LOCAL_MIN_CHARGES).text
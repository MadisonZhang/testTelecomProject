from utilities.constants import MAX_WAIT_INTERVAL
from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class AddTariffPlan(BasePage):
    MONTHLY_RENTAL = (By.XPATH, "//input[@id='rental1']")
    FREE_LOCAL_MINUTES = (By.ID, "local_minutes")
    FREE_INTERNATIONAL_MINUTES = (By.ID, "inter_minutes")
    FREE_SMS_PACK = (By.ID, "sms_pack")
    LOCAL_PER_MIN_CHARGE = (By.ID, "minutes_charges")
    INTERNATIONAL_PER_MIN_CHARGE = (By.ID, "inter_charges")
    SMS_PER_CHARGE = (By.ID,"sms_charges")
    SUBMIT_BUTTON = (By.NAME, "submit")
    RESET_BUTTON = (By.XPATH, "//li[@input='reset'")

    def fill_monthly_rental(self, monthly_rental):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.MONTHLY_RENTAL).send_keys(monthly_rental)

    def fill_free_local_min(self, free_local_min):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.FREE_LOCAL_MINUTES).send_keys(free_local_min)

    def fill_free_inter_min(self, free_inter_min):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.FREE_INTERNATIONAL_MINUTES).send_keys(free_inter_min)

    def fill_free_sms(self, free_sms):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.FREE_SMS_PACK).send_keys(free_sms)

    def fill_local_min(self, local_min):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LOCAL_PER_MIN_CHARGE).send_keys(local_min)

    def fill_inter_min(self, inter_min):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.INTERNATIONAL_PER_MIN_CHARGE).send_keys(inter_min)

    def fill_sms_charge(self, sms_charge):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SMS_PER_CHARGE).send_keys(sms_charge)

    def click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SUBMIT_BUTTON).click()

    def click_reset_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.RESET_BUTTON).click()
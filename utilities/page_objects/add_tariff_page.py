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
    RESET_BUTTON = (By.XPATH, "//section[@id='main']/div/form/div/div[36]/ul/li[2]/input")

    ALERT_RENTAL = (By.XPATH, "//label[@id='message2']")
    ALERT_FREE_LOCAL_MINUTES = (By.XPATH, "//label[@id='message3']")
    ALERT_FREE_INTERNATIONAL_MINUTES = (By.XPATH, "//label[@id='message4']")
    ALERT_FREE_SMS_PACK = (By.XPATH, "//label[@id='message5']")
    ALERT_LOCAL_PER_MIN_CHARGE = (By.XPATH, "//label[@id='message6']")
    ALERT_INTERNATIONAL_PER_MIN_CHARGE = (By.XPATH, "//label[@id='message7']")
    ALERT_SMS_PER_CHARGE = (By.XPATH, "//label[@id='message8']")

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

    def get_rental_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_RENTAL).text

    def get_free_local_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_FREE_LOCAL_MINUTES).text

    def get_free_int_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_FREE_INTERNATIONAL_MINUTES).text

    def get_free_sms_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_FREE_SMS_PACK).text

    def get_local_min_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_LOCAL_PER_MIN_CHARGE).text

    def get_inter_min_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_INTERNATIONAL_PER_MIN_CHARGE).text

    def get_sms_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ALERT_SMS_PER_CHARGE).text

    def invalid_plan_info_alert(self):
        return self.explicitly_wait_alert(MAX_WAIT_INTERVAL).text
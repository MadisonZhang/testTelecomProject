from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.constants import MAX_WAIT_INTERVAL

class AssignPlan(BasePage):
    SELECT_PLAN = (By.XPATH,"//section[@id='main']/div/form/div[1]/table/tbody/tr/td[1]")
    APPROVED_MONTHLY_RENTAL = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[2]/b")
    APPROVED_FREE_LOCAL_MINUTES = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[3]/b")
    APPROVED_FREE_INTERNATIONAL_MINUTES = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[4]/b")
    APPROVED_FREE_SMS_PACK = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[5]/b")
    APPROVED_LOCAL_PER_MIN_CHARGE = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[6]/b")
    APPROVED_INTERNATIONAL_PER_MIN_CHARGE = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[7]/b")
    APPROVED_SMS_PER_CHARGE = (By.XPATH, "//section[@id='main']/div/form/div[1]/table/tbody/tr/td[8]/b")
    TEST_MONTHLY_RENTAL = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[1]/b")
    TEST_FREE_LOCAL_MINUTES = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[2]/b")
    TEST_FREE_INTERNATIONAL_MINUTES = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[3]/b")
    TEST_FREE_SMS_PACK = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[4]/b")
    TEST_LOCAL_PER_MIN_CHARGE = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[5]/b")
    TEST_INTERNATIONAL_PER_MIN_CHARGE = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[6]/b")
    TEST_SMS_PER_CHARGE = (By.XPATH, "//section[@id='main']/div/div/table/tbody[1]/tr/td[7]/b")
    SUBMIT_BUTTON = (By.XPATH,"//section[@id='main']/div/form/div[2]/input")

    def select_approved_plan(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SELECT_PLAN).click()

    def get_approved_monthly_rental(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_MONTHLY_RENTAL).text

    def get_approved_free_local_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_FREE_LOCAL_MINUTES).text

    def get_approved_free_inter_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_FREE_INTERNATIONAL_MINUTES).text

    def get_approved_free_sms(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_FREE_SMS_PACK).text

    def get_approved_local_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_LOCAL_PER_MIN_CHARGE).text

    def get_approved_inter_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_INTERNATIONAL_PER_MIN_CHARGE).text

    def get_approved_sms_charge(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPROVED_SMS_PER_CHARGE).text

    def get_test_monthly_rental(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_MONTHLY_RENTAL).text

    def get_test_free_local_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_FREE_LOCAL_MINUTES).text

    def get_test_free_inter_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_FREE_INTERNATIONAL_MINUTES).text

    def get_test_free_sms(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_FREE_SMS_PACK).text

    def get_test_local_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_LOCAL_PER_MIN_CHARGE).text

    def get_test_inter_min(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_INTERNATIONAL_PER_MIN_CHARGE).text

    def get_test_sms_charge(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.TEST_SMS_PER_CHARGE).text

    def click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SUBMIT_BUTTON).click()
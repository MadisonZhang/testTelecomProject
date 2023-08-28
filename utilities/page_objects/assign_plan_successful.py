from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.constants import MAX_WAIT_INTERVAL

class AssignPlanSuccessfulPage(BasePage):
    CONFIRM_MSG = (By.XPATH, "//section[@id='main']/div/h2")
    HOME_LINK = (By.XPATH,"//*[@id='main']/div/ul/li/a")

    def get_plan_assigned_msg(self):
        msg = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CONFIRM_MSG).text
        return msg

    def click_navigate_to_home_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HOME_LINK).click()
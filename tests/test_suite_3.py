from test_units import *
from utilities.constants import TEST_SITE_URL, LETTER_TEL, SPECIAL_CHARAC_TEL
from utilities.page_objects.add_tariff_page import AddTariffPlan
from utilities.page_objects.index_page import IndexPage
import time
from selenium.common.exceptions import TimeoutException

class TestTelecomProject_3:
    # Test case 1 (Verifying adding new plan: all fields have to be filled)
    def test_add_new_plan(self, driver):
        print("Test Case 1 - Self ID:", id(self))
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_add_plan_button()
        try:
            add_tariff_page = AddTariffPlan(driver)
            add_tariff_page.fill_monthly_rental("")
        except TimeoutException:
            # in case of ads pop-out, refresh the page and click again
            driver.refresh()
            index_page.wait_and_click_add_plan_button()
            add_tariff_page = AddTariffPlan(driver)
            add_tariff_page.fill_monthly_rental("")
        add_tariff_page = AddTariffPlan(driver)
        # Blank field, characters, special characters can not be accepted
        add_tariff_page.fill_free_local_min(LETTER_TEL)
        add_tariff_page.fill_free_inter_min(SPECIAL_CHARAC_TEL)
        add_tariff_page.fill_free_sms(LETTER_TEL)
        add_tariff_page.fill_local_min(SPECIAL_CHARAC_TEL)
        add_tariff_page.fill_inter_min("")
        add_tariff_page.fill_sms_charge(LETTER_TEL)
        time.sleep(5)

        assert add_tariff_page.get_rental_alert() == "Number must not be blank"
        assert add_tariff_page.get_free_local_alert() == "Characters are not allowed"
        assert add_tariff_page.get_free_int_alert() == "Special characters are not allowed"
        assert add_tariff_page.get_free_sms_alert() == "Characters are not allowed"
        assert add_tariff_page.get_local_min_alert() == "Special characters are not allowed"
        assert add_tariff_page.get_inter_min_alert() == "Number must not be blank"
        assert add_tariff_page.get_sms_alert() == "Characters are not allowed"

        add_tariff_page.click_submit_button()
        assert add_tariff_page.invalid_plan_info_alert() == "please fill all fields Correct Value"
        time.sleep(2)
        add_tariff_page.click_accept_alert()
        # Click reset button will clear all filled fields
        add_tariff_page.click_reset_button()
        time.sleep(2)
        add_tariff_page.click_submit_button()
        assert add_tariff_page.invalid_plan_info_alert() == "please fill all fields Correct Value"
        # end of test case 1



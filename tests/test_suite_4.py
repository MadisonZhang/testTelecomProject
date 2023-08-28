import time

from utilities.constants import TEST_SITE_URL, MADE_UP_CUSTOMER_ID, SPECIAL_CHARAC_CUSTOMER_ID, \
    LETTER_CUSTOMER_ID, ADD_PLAN_CUSTOMER_LOOK_UP_URL
from utilities.page_objects.customer_look_up_page import CustomerLookUp
from utilities.page_objects.index_page import IndexPage


class TestTelecomProject_4:
    # Test case 1: Verifying only valid customer id will be accepted
    def test_customer_look_up(self,driver):
        print("Test Case 1 - Self ID:", id(self))
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_add_plan_to_customer()
        # in case of ads pop-out, refresh the page and click again
        driver.refresh()
        index_page.wait_and_click_add_plan_to_customer()

        customer_look_up_page = CustomerLookUp(driver)
        # Blank customer id will trigger warning and cannot be submitted
        customer_look_up_page.fill_customer_id("")
        customer_look_up_page.click_background()
        customer_id_warning_msg = customer_look_up_page.get_warning_msg()
        assert customer_id_warning_msg.__contains__("blank"), "Number must not be blank"
        customer_look_up_page.click_submit_button()
        submit_failed_msg = customer_look_up_page.invalid_customer_id_alert()
        assert submit_failed_msg == "Please Correct Value Input", "Alert message successfully displayed on popped out window"

        # Customer ID containing special character will trigger warning and cannot be submitted
        time.sleep(2)
        customer_look_up_page.click_accept_alert()
        customer_look_up_page.clear_customer_id_field()
        customer_look_up_page.fill_customer_id(SPECIAL_CHARAC_CUSTOMER_ID)
        time.sleep(5)
        customer_id_warning_msg = customer_look_up_page.get_warning_msg()
        assert customer_id_warning_msg.__contains__("Special characters")
        customer_look_up_page.click_submit_button()
        submit_failed_msg = customer_look_up_page.invalid_customer_id_alert()
        assert submit_failed_msg == "Please Correct Value Input", "Alert message successfully displayed on popped out window"

        # Customer ID containing letter will trigger warning and cannot be submitted
        time.sleep(2)
        customer_look_up_page.click_accept_alert()
        customer_look_up_page.clear_customer_id_field()
        customer_look_up_page.fill_customer_id(LETTER_CUSTOMER_ID)
        time.sleep(5)
        customer_id_warning_msg = customer_look_up_page.get_warning_msg()
        assert customer_id_warning_msg == "Characters are not allowed"
        customer_look_up_page.click_submit_button()
        submit_failed_msg = customer_look_up_page.invalid_customer_id_alert()
        assert submit_failed_msg == "Please Correct Value Input", "Alert message successfully displayed on popped out window"

        # Made up customer ID will not proceed to next step
        time.sleep(2)
        customer_look_up_page.click_accept_alert()
        customer_look_up_page.clear_customer_id_field()
        customer_look_up_page.fill_customer_id(MADE_UP_CUSTOMER_ID)
        customer_look_up_page.click_submit_button()
        time.sleep(5)
        assert customer_look_up_page.get_current_url() == ADD_PLAN_CUSTOMER_LOOK_UP_URL
        prompt_label = customer_look_up_page.alert_to_input_correct_id()
        assert prompt_label == "Please Input Your Correct Customer ID"





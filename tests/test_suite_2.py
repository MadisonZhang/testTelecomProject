import time
from utilities.constants import TEST_SITE_URL, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL, VALID_ADDRESS, \
    VALID_TEL_NUMBER, NUMBER_NAME, SPECIAL_CHARAC_NAME, INVALID_EMAIL, INVALID_ADDRESS, LETTER_TEL, SPECIAL_CHARAC_TEL
from utilities.page_objects.add_customer_page import AddCustomerPage
from utilities.page_objects.index_page import IndexPage


class TestTelecomProject_2:
    # Test case 1 (Verifying adding new customer: all fields have to be filled)

    def test_add_new_customer(self, driver):
        print("Test Case 1 - Self ID:", id(self))
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_add_customer_button()
        # in case of ads pop-out, refresh the page and click again
        driver.refresh()
        index_page.wait_and_click_add_customer_button()

        add_customer_page = AddCustomerPage(driver)
        # Invalid fill will trigger warning and cannot be submitted
        add_customer_page.fill_customer_first_name(NUMBER_NAME)
        add_customer_page.fill_customer_last_name(SPECIAL_CHARAC_NAME)
        time.sleep(1)
        add_customer_page.fill_customer_email(INVALID_EMAIL)
        add_customer_page.fill_customer_address(INVALID_ADDRESS)
        add_customer_page.fill_customer_tel_number(LETTER_TEL)
        time.sleep(1)
        assert add_customer_page.invalid_fn_alert() == "Numbers are not allowed"
        assert add_customer_page.invalid_ln_alert() == "Special characters are not allowed"
        assert add_customer_page.invalid_email_alert() == "Email-ID is not valid"
        assert add_customer_page.invalid_address_alert() == "Special characters are not allowed"
        assert add_customer_page.invalid_tel_alert() == "Characters are not allowed"
        add_customer_page.click_submit_button()
        assert add_customer_page.invalid_customer_info_alert() == "please fill all fields"
        time.sleep(2)
        add_customer_page.click_accept_alert()
        add_customer_page.clear_tel_field()
        add_customer_page.fill_customer_tel_number(SPECIAL_CHARAC_TEL)
        time.sleep(2)
        assert add_customer_page.invalid_tel_alert() == "Special characters are not allowed"
        add_customer_page.click_submit_button()
        assert add_customer_page.invalid_customer_info_alert() == "please fill all fields"
        time.sleep(2)
        add_customer_page.click_accept_alert()
        # Click reset button will clear all filled fields
        add_customer_page.click_reset_button()
        time.sleep(2)
        add_customer_page.click_submit_button()
        assert add_customer_page.invalid_customer_info_alert() == "please fill all fields"
        # end of test case 1
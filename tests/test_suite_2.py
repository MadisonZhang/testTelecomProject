import time
from utilities.constants import TEST_SITE_URL, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL, VALID_ADDRESS, \
    VALID_TEL_NUMBER
from utilities.page_objects.add_customer_page import AddCustomerPage
from utilities.page_objects.add_customer_successful_page import AddCustomerSuccessfulPage
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
        add_customer_page.click_background_done()
        add_customer_page.fill_customer_first_name(VALID_FIRST_NAME)
        add_customer_page.fill_customer_last_name(VALID_LAST_NAME)
        add_customer_page.fill_customer_email(VALID_EMAIL)
        add_customer_page.fill_customer_address(VALID_ADDRESS)
        add_customer_page.fill_customer_tel_number(VALID_TEL_NUMBER)
        time.sleep(5)
        add_customer_page.click_reset_button()
        add_customer_page.click_submit_button()
        assert

        # end of test case 1
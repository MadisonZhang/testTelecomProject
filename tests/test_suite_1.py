from test_units import *
import pytest

from utilities.constants import TEST_SITE_URL, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL, VALID_ADDRESS, \
    VALID_TEL_NUMBER, VALID_MONTHLY_RENTAL, VALID_FREE_LOCAL_MINUTES, VALID_FREE_INTERNATIONAL_MINUTES, \
    VALID_FREE_SMS_PACK, VALID_LOCAL_PER_MIN_CHARGE, VALID_INTERNATIONAL_PER_MIN_CHARGE, VALID_SMS_PER_CHARGE, \
    APPROVED_SMS_PER_CHARGE, APPROVED_INTERNATIONAL_PER_MIN_CHARGE, APPROVED_LOCAL_PER_MIN_CHARGE, \
    APPROVED_FREE_SMS_PACK, APPROVED_FREE_INTERNATIONAL_MINUTES, APPROVED_FREE_LOCAL_MINUTES, APPROVED_MONTHLY_RENTAL
from utilities.page_objects.add_customer_page import AddCustomerPage
from utilities.page_objects.add_customer_successful_page import AddCustomerSuccessfulPage
from utilities.page_objects.assign_plan_successful import AssignPlanSuccessfulPage
from utilities.page_objects.assign_plan_to_customer_page import AssignPlan
from utilities.page_objects.billing_customer_page import PayBilling
from utilities.page_objects.customer_look_up_page import CustomerLookUp
from utilities.page_objects.add_tariff_page import AddTariffPlan
from utilities.page_objects.add_tariff_successful_page import AddTariffSuccessfulPage
from utilities.page_objects.index_page import IndexPage
import time

class TestTelecomProject_1:
    # Test case 1 (Verifying adding new customer)

    @pytest.mark.run(order=1)
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
        add_customer_page.click_submit_button()

        add_customer_successful_page = AddCustomerSuccessfulPage(driver)
        self.__class__.customer_id_label = add_customer_successful_page.get_customer_id()
        print(self.__class__.customer_id_label)
        assert self.__class__.customer_id_label is not None, f"Customer successfully added with id {self.__class__.customer_id_label}"
        # end of test case 1

    # Test case 2 (Verifying adding new tariff plan)
    @pytest.mark.run(order=2)
    def test_add_new_plan(self,driver):
        print("Test Case 2 - Self ID:", id(self))
        add_customer_successful_page = AddCustomerSuccessfulPage(driver)
        add_customer_successful_page.click_navigate_to_home_button()

        index_page = IndexPage(driver)
        index_page.wait_and_click_add_plan_button()

        add_tariff_page = AddTariffPlan(driver)
        add_tariff_page.fill_monthly_rental(VALID_MONTHLY_RENTAL)
        add_tariff_page.fill_free_local_min(VALID_FREE_LOCAL_MINUTES)
        add_tariff_page.fill_free_inter_min(VALID_FREE_INTERNATIONAL_MINUTES)
        add_tariff_page.fill_free_sms(VALID_FREE_SMS_PACK)
        add_tariff_page.fill_local_min(VALID_LOCAL_PER_MIN_CHARGE)
        add_tariff_page.fill_inter_min(VALID_INTERNATIONAL_PER_MIN_CHARGE)
        add_tariff_page.fill_sms_charge(VALID_SMS_PER_CHARGE)
        time.sleep(5)
        add_tariff_page.click_submit_button()

        add_plan_successful_page = AddTariffSuccessfulPage(driver)
        plan_added_label = add_plan_successful_page.get_tariff_added_msg()
        assert  plan_added_label.__contains__("Congratulation"), "Tariff plan added successfully"
        # end of test case 2

    # Test case 3 (Verifying adding plan to designated customer)
    @pytest.mark.run(order=3)
    def test_add_plan_to_customer(self, driver):
        print("Test Case 3 - Self ID:", id(self))
        add_plan_successful_page = AddTariffSuccessfulPage(driver)
        add_plan_successful_page.click_navigate_to_home_button()
        # in case of ads pop-out, refresh the page and click again
        # driver.refresh()
        # add_plan_successful_page.click_navigate_to_home_button()

        index_page = IndexPage(driver)
        index_page.wait_and_click_add_plan_to_customer()

        customer_look_up_page = CustomerLookUp(driver)
        customer_look_up_page.fill_customer_id(TestTelecomProject_1.customer_id_label)
        time.sleep(5)
        customer_look_up_page.click_submit_button()

        assign_plan_page = AssignPlan(driver)
        assert int(assign_plan_page.get_approved_monthly_rental()) == APPROVED_MONTHLY_RENTAL
        assert int(assign_plan_page.get_approved_free_local_min()) == APPROVED_FREE_LOCAL_MINUTES
        assert int(assign_plan_page.get_approved_free_inter_min()) == APPROVED_FREE_INTERNATIONAL_MINUTES
        assert int(assign_plan_page.get_approved_free_sms()) == APPROVED_FREE_SMS_PACK
        assert int(assign_plan_page.get_approved_local_min()) == APPROVED_LOCAL_PER_MIN_CHARGE
        assert int(assign_plan_page.get_approved_inter_min()) == APPROVED_INTERNATIONAL_PER_MIN_CHARGE
        assert int(assign_plan_page.get_approved_sms_charge()) == APPROVED_SMS_PER_CHARGE

        assert int(assign_plan_page.get_test_monthly_rental()) == VALID_MONTHLY_RENTAL
        assert int(assign_plan_page.get_test_free_local_min()) == VALID_FREE_LOCAL_MINUTES
        assert int(assign_plan_page.get_test_free_inter_min()) == VALID_FREE_INTERNATIONAL_MINUTES
        assert int(assign_plan_page.get_test_free_sms()) == VALID_FREE_SMS_PACK
        assert int(assign_plan_page.get_test_local_min()) == VALID_LOCAL_PER_MIN_CHARGE
        assert int(assign_plan_page.get_test_inter_min()) == VALID_INTERNATIONAL_PER_MIN_CHARGE
        assert int(assign_plan_page.get_test_sms_charge()) == VALID_SMS_PER_CHARGE

        assign_plan_page.select_approved_plan()
        time.sleep(5)
        assign_plan_page.click_submit_button()

        assign_successful_page = AssignPlanSuccessfulPage(driver)
        plan_assigned_label = assign_successful_page.get_plan_assigned_msg()
        assert plan_assigned_label == "Congratulation Tariff Plan assigned"
        # end of test case 3

    @pytest.mark.run(order=4)
    def test_pay_billing(self,driver):
        print("Test Case 4 - Self ID:", id(self))
        assign_successful_page = AssignPlanSuccessfulPage(driver)
        assign_successful_page.click_navigate_to_home_button()

        index_page = IndexPage(driver)
        index_page.wait_and_click_billing()

        customer_look_up_page = CustomerLookUp(driver)
        customer_look_up_page.fill_customer_id(TestTelecomProject_1.customer_id_label)
        time.sleep(5)
        customer_look_up_page.click_submit_button()

        pay_billing_page = PayBilling(driver)
        customer_info_label = pay_billing_page.get_customer_info()
        assert customer_info_label.__contains__(TestTelecomProject_1.customer_id_label), "Customer id is successfully retrieved."
        assert customer_info_label.__contains__(VALID_FIRST_NAME), "Customer name is successfully retrieved."
        time.sleep(5)
        local_min_usage_charge = int(pay_billing_page.get_local_min_charges())
        int_min_usage_charge = int(pay_billing_page.get_int_min_charges())
        sms_usage_charge = int(pay_billing_page.get_sms_charges())
        usage_charge = int(pay_billing_page.get_usage_charges())
        assert usage_charge == (local_min_usage_charge + int_min_usage_charge + sms_usage_charge), "Usage charge calculation correct"
        customer_plan_rental = int(pay_billing_page.get_monthly_rental())
        total_billing = int(pay_billing_page.get_total_billing())
        assert total_billing == (usage_charge + customer_plan_rental), "Total billing calculation correct"
        # end of test case 4









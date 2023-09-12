# testTelecomProject

This repository contains a suite of automated test cases for a telecom project. These tests cover various aspects of the telecom system, including customer creation, data plan setup, plan assignment, and billing processes.

## Test Cases

1. **Customer Creation**: This test case ensures the accurate creation of customer profiles, validating user inputs and triggering appropriate alerts for invalid data.

2. **Data Plan Setup**: This test case validates the setup of data plans, verifying that all required numeric values for SMS, local minutes, and international minutes are correctly saved.

3. **Plan Assignment to Customer**: This test case verifies the successful assignment of approved data plans to created customer. It involves looking up customers with valid customer ID, selecting an appropriate plan, and confirming the assignment.

4. **Billing to Customer**: This test case simulates the billing process, which starts with looking up the customer with valid customer ID, calculating the billing amount based on monthly rental and actual usage, and ensuring the accurate generation of the total billing amount. 

## Technologies Used

- Test Automation Framework: Selenium and PyTest
- Programming Language: Python
- Testing Tool: WebDriver

Explore the test cases, contribute to the project, or customize the test suite to fit specific telecom scenarios and requirements.

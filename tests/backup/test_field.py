from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

# Create a new instance of the Firefox driver (you can use other drivers like Chrome)
driver = webdriver.Chrome()

# Open a web page with a textarea element
driver.get("https://demo.guru99.com/telecom/assigntariffplantocustomer.php")
driver.find_element(By.XPATH,"//input[@id='customer_id']").send_keys("")
driver.find_element(By.XPATH,"//section[@id='main']/div/form/div/div[2]/h3").click()

time.sleep(3)
driver.find_element(By.NAME, "submit").click()
time.sleep(3)
driver.switch_to.alert.accept()

# Use send_keys() to enter text into the textarea


# Close the browser window
driver.quit()

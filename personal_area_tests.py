import time
import unittest
from log_in_test import log_in
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from driver_set_up import driver_set_up

class Testcase(unittest.TestCase):

    def setUp(self):
        self.driver = driver_set_up()
        self.driver.get('http://qa.trado.ai/')
        log_in(self.driver)
        go_to_pa = WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[1]/a"))))
        go_to_pa.click()

    def tearDown(self):
        self.driver.close()

    def test_delivery_details(self):
        """
        a test for the delivery details of the user
        :return:
        """

        edit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[4]')))
        edit.click()
        time.sleep(2)

        first_name_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[1]/span/input')))
        first_name_element.click()
        first_name_element.send_keys("Moshe")

        time.sleep(2)

        last_name_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[2]/span/input')))
        last_name_element.click()
        last_name_element.send_keys("Levi")

        email_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[4]/span/input')))
        email_element.click()
        email_element.send_keys("moshe123@gmail.com")
        time.sleep(2)

        city_and_street = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[1]/input')))
        city_and_street.click()
        city_and_street.send_keys("city/st")
        time.sleep(2)

        street_num = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[2]/span/input')))
        street_num.click()
        street_num.send_keys("8")
        time.sleep(2)

        zip_code = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[2]/span/input')))
        zip_code.click()
        zip_code.send_keys("81234132")
        time.sleep(2)

        save_details_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/input')))
        save_details_btn.click()

    def test_my_wallet(self):
        """
        testing withdrawal from the E-Wallet
        :return:
        """

        withdraw_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/section/button')))
        withdraw_btn.click()
        time.sleep(2)

    def test_contact_us_navigation(self):

        contact_us_btns = [
            '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/span/a/label',
            '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[4]/div[3]/span/a/label',
            '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/span/a/label',
            '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/span/a/label'
        ]

        wait = WebDriverWait(self.driver, 10)

        for btn in contact_us_btns:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, btn)))
                element.click()
                print(f"Clicked on element: {btn}")

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {btn} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()









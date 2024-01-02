import time
import unittest
from test_log_in import log_in
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
        go_to_products = WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[9]/div/a/div'))))
        go_to_products.click()

    def tearDown(self):
        self.driver.close()

    def test1_arrows(self):

        go_left = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div[2]')))
        go_left.click()
        time.sleep(2)

        go_right = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]')))
        go_right.click()

    def test2_items_in_importing(self):

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[2]/div/div[2]/div[2]/div[3]',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[3]/div/div[2]/div[2]/div[2]/div']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test3_items_in_PM(self):

        time.sleep(2)
        go_to_PM = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[10]/div/a/div/div')))
        go_to_PM.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div/div[2]/div[2]/div[1]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test4_items_in_zxczxczx(self):

        time.sleep(2)
        go_to_zxc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[11]/div/a/div/div')))
        go_to_zxc.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div/div[2]/div[2]/div[1]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test5_items_in_beers(self):

        time.sleep(2)
        go_to_beers = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[12]/div/a/div/div')))
        go_to_beers.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[2]/div/div[2]/div[2]/div[3]',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[3]/div/div[2]/div[2]/div[3]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()


    def test6_items_in_snacks(self):

        time.sleep(2)
        go_to_snacks = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[13]/div/a/div/div')))
        go_to_snacks.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div/div[2]/div[2]/div[3]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test7_go_to_kanabis(self):

        go_left = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div[2]')))
        for _ in range(3):
            go_left.click()
        time.sleep(2)

        time.sleep(2)
        go_to_kanabis = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[14]/div/a/div/div')))
        go_to_kanabis.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[2]/div/div[2]/div[2]/div[3]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)
                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test8_go_to_wagwan(self):

        go_left = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div[2]')))
        for _ in range(3):
            go_left.click()

        time.sleep(2)
        go_to_wagwan = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[15]/div/a/div/div')))
        go_to_wagwan.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()


    def test9_go_to_drinks(self):

        time.sleep(2)
        go_to_snacks = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[13]/div/a/div/div')))
        go_to_snacks.click()

        time.sleep(2)
        go_to_drinks = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[16]/div/a/div/div')))
        go_to_drinks.click()

        time.sleep(2)
        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                time.sleep(2)
                item_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]/i'))).click()
                time.sleep(3)
                item_remove = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/div/span[2]'))).click()
                time.sleep(3)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()



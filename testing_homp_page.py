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

    def tearDown(self):
        self.driver.close()

    def test1_logo(self):

        """
        Testing app's logo's functionality.
        :return:
        """
        click_logo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[2]/a/div/a/img")))
        click_logo.click()

    def test2_search_engine(self):
        """
        Testing apps search engine.
        :return:
        """
        print("vlad")
        click_search_engine = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[2]/div/span/input'))).send_keys('sldkjfm')
        time.sleep(1)
        click_search_logo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[2]/div/div[2]/img"))).click()


    def test3_go_to_personal_area(self):
        """
        Testing navigation to personal area.
        :return:
        """
        go_to_pa = WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[1]/a"))))
        go_to_pa.click()

    def test4_go_to_item_categories(self):
        """
        Testing navigation to item categories.
        In order to navigate to the item categories page you need to press an item and not a button to lead you there.
        :return:
        """
        item_categories = ['/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[9]/div/a/div',
                           '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[10]/div/a/div',
                           '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[11]/div/a/div',
                           '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[12]/div/a/div',
                           '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[13]/div/a/div']

        for item in item_categories:
            try:
                click_items = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, item)))
                click_items.click()

                # Add additional checks or actions on the new page if needed

                # Navigate back to the original page
                self.driver.back()
            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")



    def test5_go_to_item_upload(self):
        """
        Testing navigation to item upload
        :return:
        """
        go_to_item_upload = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[1]/button')))
        go_to_item_upload.click()

    def test6_switch_lang(self):
        """
        Testing switching language feature
        :return:
        """
        switch_lang = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]')))
        switch_lang.click()

    def test7_go_to_accessibility(self):
        """
        testing navigation to accessibility page
        :return:
        """
        try:
            go_to_accessibility = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'enable-trigger-circle')))
            go_to_accessibility.click()
        except TimeoutException:
            print("Element 'enable-trigger-circle' not found or not clickable within the specified time.")

    def test8_footer(self):
        """
        Testing navigation through footer links
        :return:
        """
        footer_links = ['//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[1]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[2]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[3]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[4]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[1]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[2]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[3]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[4]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[1]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[2]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[3]'
                        ]

        for link in footer_links:
            footer_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
            footer_click.click()

    def test9_logout(self):
        """
        Testing Logout functionality
        :return:
        """
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a/span')))
        logout_btn.click()
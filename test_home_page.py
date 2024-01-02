import time
import unittest
from log_in import log_in
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from driver_set_up import driver_set_up
import pyautogui

class Testcase(unittest.TestCase):

    def setUp(self):
        self.driver = driver_set_up()
        self.driver.get('http://qa.trado.ai/')
        log_in(self.driver)



    def test1_logo(self):

        """
        Testing app's logo's functionality.
        :return:
        """
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[10]/div/a"))).click()
        time.sleep(1)
        click_logo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[2]/header/div/div/div[2]/a/div/a/img"))).click()
        assert True

    def test2_search_engine(self):
        """
        Testing apps search engine.
        :return:
        """
        click_search_engine = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[2]/div/span/input'))).click()
        click_search_engine = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[2]/div/span/input'))).send_keys('f')
        time.sleep(2)
        click_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[2]/div/div[1]/div/a[1]/div '))).click()
        txt_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div/div[1]/div[1]/div/h1'))).text
        assert txt_element == "Fsafsfsafsa"

    def test3_go_to_personal_area(self):
        """
        Testing navigation to personal area.
        :return:
        """
        go_to_pa = WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[1]/a"))))
        go_to_pa.click()
        assert True

    def test4_go_to_item_categories(self):
        """
        Testing navigation to item categories.
        In order to navigate to the item categories page you need to press an item and not a button to lead you there.
        :return:
        """
        click_items = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[9]/div/a/div")))
        click_items.click()
        item_txt = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/span/h1"))).text
        assert item_txt == "ייבוא"
    def test5_go_to_item_upload(self):
        """
        Testing navigation to item upload
        :return:
        """
        go_to_item_upload = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[1]/button')))
        go_to_item_upload.click()
        assert True

    def test6_switch_lang(self):
        """
        Testing switching language feature
        :return:
        """
        before_txt = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[1]/a'))).text
        switch_lang = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]'))).click()
        time.sleep(1)
        after_txt = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[1]/a'))).text
        assert before_txt != after_txt

    def test7_go_to_accessibility(self):
        """
        testing navigation to accessibility page
        :return:
        """
        accessibility_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'enable-toolbar-trigger'))).click()
        assert True
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
        assert True

    def test9_logout(self):
        """
        Testing Logout functionality
        :return:
        """
        pyautogui.moveTo(175, 220, duration=1)
        time.sleep(2)
        logout_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/header/div/div/a')))
        logout_btn.click()
        assert True
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import mongoScrape
from pa import password, db_name, user_name
from mongoScrape import encoded_password
import mongoScrape
from driver_set_up import driver_set_up
import unittest
import random


class Testcase(unittest.TestCase):

    def setUp(self):
        self.driver = driver_set_up()
        self.driver.get('http://qa.trado.ai/')

    def tearDown(self):
        self.driver.close()

    def test_sign_in(self):
        #locate and click on register login
        div_element_login_register = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a')))
        div_element_login_register.click()

        #switch to sign in
        sign_in_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[1]/span[2]'))).click()
        time.sleep(1)

        # phone to be used
        phone = random.randint(0000000,9999999)


        phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))
        phone_input.clear()
        phone_input.send_keys(f'{phone}')

        #fill the employers num field
        emp_num = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'))).send_keys("123456")

        #fill guidelines acceptance check
        gl_check = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/label'))).click()

        #press enter
        enter_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'))).click()

        time.sleep(5)
        client = mongoScrape.create_mongo_connection(user_name, encoded_password, db_name)
        db = mongoScrape.create_mongo_db(client, db_name)
        code = mongoScrape.get_loginCode(db, f'972{phone}')

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal_modal')))
        input_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'))).send_keys(code)
        time.sleep(1)
        submit_btn2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form_submitBtn'))).click()




    def modify_phone_number(self, phone):
        # Modify the phone number by changing one digit
        # You can customize this part based on your requirements
        modified_number = list(phone)
        # Change the last digit, for example
        modified_number[-1] = str((int(modified_number[-1]) + 1) % 10)
        return ''.join(modified_number)



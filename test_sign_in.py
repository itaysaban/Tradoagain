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
        sign_in_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[1]/span[2]')))
        sign_in_btn.click()
        time.sleep(1)

        # phone to be used
        phone = '00123458'

        while True:
            # locate phone field and send keys
            phone_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))
            phone_input.clear()
            phone_input.send_keys(f'972{phone}')

            # locate phone field and send keys
            phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))).send_keys(phone)

            #fill the employers num field
            emp_num = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'))).send_keys("123456")

            #fill guidelines acceptance check
            gl_check = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/label'))).click()

            #press enter
            enter_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[4]/input'))).click()


            time.sleep(5)
            phone = '00123458'
            phone_to_use = f'972{phone}'
            # handle the code aquiring
            client = mongoScrape.create_mongo_connection(user_name, encoded_password, db_name)
            db = mongoScrape.create_mongo_db(client, db_name)
            code = mongoScrape.get_loginCode(db, f'972{phone}')
            print(f'login code: {code}')

            # Wait for the modal to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal_modal')))

            # Interact with each input element

            input_class = 'input_0'
            input_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')))
            # Debugging: Check if element is visible and enabled
            print(f"Element {input_class} is displayed: {input_element.is_displayed()}")
            print(f"Element {input_class} is enabled: {input_element.is_enabled()}")
            input_element.send_keys(code)

            time.sleep(1)
            submit_btn2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form_submitBtn'))).click()

            # Check if sign-in was successful
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'success_message')))
                print("Sign-in successful!")
                break  # Break out of the loop if sign-in is successful
            except Exception as e:
                print(f"Sign-in failed with phone number {phone}. Trying with a modified number.")
                # Modify the phone number for the next iteration
                phone = self.modify_phone_number(phone)

        return self.driver

    def modify_phone_number(self, phone):
        # Modify the phone number by changing one digit
        # You can customize this part based on your requirements
        modified_number = list(phone)
        # Change the last digit, for example
        modified_number[-1] = str((int(modified_number[-1]) + 1) % 10)
        return ''.join(modified_number)



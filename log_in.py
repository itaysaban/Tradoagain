import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import mongoScrape
from pa import password, db_name, user_name
from mongoScrape import encoded_password
import mongoScrape
from driver_set_up import driver_set_up


# driver = driver_set_up()

def log_in(driver):
    #locate and click on register login
    div_element_login_register = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="root"]/div/div[2]/div/section/nav/div/div[2]/a')))
    div_element_login_register.click()


    # phone to be used
    phone = '00123456'

    # locate phone field and send keys
    phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control'))).send_keys(phone)

    # click submit to move to enter code
    submit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form_submitBtn'))).click()

    time.sleep(2)
    phone = '00123456'
    phone_to_use = f'972{phone}'
    # handle the code aquiring
    client = mongoScrape.create_mongo_connection(user_name, encoded_password, db_name)
    db = mongoScrape.create_mongo_db(client, db_name)
    code = mongoScrape.get_loginCode(db, '97200123456')

    # Wait for the modal to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal_modal')))

    # Interact with each input element

    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'))).send_keys(code)
    submit_btn2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form_submitBtn'))).click()



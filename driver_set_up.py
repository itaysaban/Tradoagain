
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
# setUp the driver

def driver_set_up():
    chrome_options = ChromeOptions()
    # chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('disable_extensions')

    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    # driver.get('http://qa.trado.ai/')
    driver.maximize_window()

    return driver
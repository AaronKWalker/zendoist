from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic import info
import os
from logic import zendesk

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

# driver = webdriver.Chrome(options = chrome_options, executable_path = chrome_driver)
# driver.get(info.z_url)

zendesk = zendesk.Zendesk(Options, webdriver, chrome_driver, info)
zendesk.call_zdesk()
zendesk.verify_page()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

driver = webdriver.Chrome(options = chrome_options, executable_path = chrome_driver)
driver.get("https://sailpointsupport.zendesk.com/agent/filters/360185627271")

driver.get_screenshot_as_file("capture.png")
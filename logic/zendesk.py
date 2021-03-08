from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Zendesk:
    def __init__(self, chrome_driver, info):
        self.Options = Options
        self.options = self.Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920x1080")
        self.chrome_driver = chrome_driver
        self.driver = webdriver.Chrome(options = self.options, executable_path = self.chrome_driver)
        self.driver.implicitly_wait(5)
        self.info = info
    
    def call_zdesk(self):
        self.driver.get(self.info.z_url)
    
    def verify_page(self):
        if (self.driver.title == 'SailPoint IdentityNow'):
            self.handle_sso()
        elif (self.driver.title == 'SailPoint Support - Agent'):
            pass
        else:
            raise ValueError('Unable to verify page')
        # REMOVE ↓
        self.driver.quit()
    
    def handle_sso(self):
        # SSO page #1
        try:
            username_tag = self.driver.find_element_by_id('username')
            password_tag = self.driver.find_element_by_id('password')
            btn_tag = self.driver.find_element_by_xpath("//button[@type='submit']/span")
        except:
            raise ValueError('Unable to find page elements on SSO page #1')
        try:
            username_tag.send_keys(self.info.user)
            password_tag.send_keys(self.info.pw)
            btn_tag.click()
            # time.sleep(7)
            # self.driver.save_screenshot("capture.png")
            # print('screenshot successful')
        except:
            raise ValueError('Unable to interact with page elements on SSO page #1')
        # SSO page #2
        try:
            duo_push_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Duo Push to iOS')]")))
        except:
            raise ValueError('Unable to find page elements on SSO page #2')
        try:
            duo_push_tag.click()
            self.driver.save_screenshot("capture.png")
            print('screenshot successful')
        except:
            raise ValueError('Unable to interact with page elements on SSO page #2')
        # SSO page #3
        try:
            send_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "")))
        except:
            raise ValueError('Unable to find page elements on SSO page #3')
        try:
            send_tag.click()
        except:
            raise ValueError('Unable to interact with page elements on SSO page #3')
        
    def set_page_elements(self):
        pass

    def done(self, c=True):
        if c:
            self.driver.close()
        else:
            self.driver.quit()
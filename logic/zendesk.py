from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os

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
    
    def handle_sso(self):
        # SSO page #1
        try:
            username_tag = self.driver.find_element_by_id('username')
            password_tag = self.driver.find_element_by_id('password')
            btn_tag = self.driver.find_element_by_xpath("//button[@type='submit']/span")
        except:
            self.screen_shot('sso_page1')
            raise ValueError('Unable to find page elements on SSO page #1')
        try:
            username_tag.send_keys(self.info.user)
            password_tag.send_keys(self.info.pw)
            btn_tag.click()
        except:
            self.screen_shot('sso_page1')
            raise ValueError('Unable to interact with page elements on SSO page #1')
        # SSO page #2
        try:
            duo_push_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Duo Push to iOS')]")))
        except:
            self.screen_shot('sso_page2')
            raise ValueError('Unable to find page elements on SSO page #2')
        try:
            duo_push_tag.click()
        except:
            self.screen_shot('sso_page2')
            raise ValueError('Unable to interact with page elements on SSO page #2')
        # SSO page #3
        try:
            send_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "Login.Submit")))
        except:
            self.screen_shot('sso_page3')
            raise ValueError('Unable to find page elements on SSO page #3')
        try:
            print('DUO REQUEST SENT.  AWAITING DUO 2FA APPROVAL')
            send_tag.click()
        except:
            self.screen_shot('sso_page3')
            raise ValueError('Unable to interact with page elements on SSO page #3')
        # verify Zendesk came up
        try:
            zdesk_title = WebDriverWait(self.driver, 30).until(lambda x: 'SailPoint Support - Agent' in self.driver.title)
            self.screen_shot('zdesk_post_sso_success')
        except:
            self.screen_shot('zdesk_post_sso')
            raise ValueError('Zendesk page not found/present')
        
    def set_page_elements(self):
        pass
    
    def screen_shot(self, filename):
        now = datetime.now()
        nownow = now.strftime('%d-%m-%Y_%H:%M:%S')
        folder = os.getcwd() + "/captures"
        self.driver.save_screenshot(folder + '/' + filename + nownow + '.png')

    def done(self, c=True):
        if c:
            self.driver.close()
        else:
            self.driver.quit()
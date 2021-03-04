class Zendesk:
    def __init__(self, Options, webdriver, chrome_driver, info):
        self.Options = Options
        self.options = self.Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920x1080")
        self.chrome_driver = chrome_driver
        self.driver = webdriver.Chrome(options = self.options, executable_path = self.chrome_driver)
        self.info = info
        self.page_title = ''
    
    def call_zdesk(self):
        self.driver.get(self.info.z_url)
    
    def verify_page(self):
        if (self.driver.title == 'SailPoint IdentityNow'):
            self.handle_sso()
        elif (self.driver.title == 'SailPoint Support - Agent'):
            #handle zendesk page scraping
        else:
            raise ValueError('Unable to verify page')
        self.driver.quit()
    
    def handle_sso(self):
        try:
            username_tag = self.driver.find_element_by_id('username')
            password_tag = self.driver.find_element_by_id('password')
        except:
            raise ValueError('Unable to find username/password elements')
        

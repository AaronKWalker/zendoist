from logic import info
from logic import zendesk
import os

chrome_driver = os.getcwd() + "\\chromedriver.exe"

zendesk = zendesk.Zendesk(chrome_driver, info)
zendesk.call_zdesk()
zendesk.verify_page()
zendesk.done(False)
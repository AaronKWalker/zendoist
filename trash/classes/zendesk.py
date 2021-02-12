import requests
import base64

class Zendesk:
    def __init__(self):
        self.b64_str = ''
        self.res = {}
    
    def b64_encode(self, str):
        str_bytes = str.encode('ascii')
        b64_bytes = base64.b64encode(str_bytes)
        self.b64_str = b64_bytes.decode('ascii')
    
    def get_req(self, url, user, pw):
        self.res = requests.get(url, auth=(user, pw))
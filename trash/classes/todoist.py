from todoist import TodoistAPI
from .info import *

class Todoist:
    def __init__(self):
        self.token = token
        self.api = TodoistAPI(self.token)
        self.api.sync()
        

    def sync(self):
        self.api.sync()
    

    def get_obj(self, obj):
        if obj == 'state':
            return self.api.state
        elif obj == 'projects':
            return self.api.state['projects']
        elif obj == 'labels':
            return self.api.state['labels']
        elif obj == 'items':
            return self.api.state['items']
        elif obj == 'sections':
            return self.api.state['sections']
        else:
            return 'Object Not Found'
    
    
    def get_items(self, p_id=False):
        all_items = self.get_obj('items')
        if p_id:
            select_items = []
            for item in all_items:
                if item['project_id'] == p_id:
                    select_items.append(item)
            all_items = select_items
        return all_items
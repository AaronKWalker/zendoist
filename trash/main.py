from classes.todoist import Todoist
from classes.zendesk import Zendesk
from classes.info import *
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

gettem = Todoist
states = gettem().get_obj('state')
projects = gettem().get_obj('projects')
sections = gettem().get_obj('sections')
items = Todoist().get_items(proj_id)

# pp(items)

zdesk = Zendesk()
r = zdesk.get_req(url, user, pw)
pp(r)
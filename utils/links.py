import os
import sys

sys.path.append(os.path.abspath('../settings/'))

from constants import DEFAULT_MENU_PAGES


def link_maker(page_id):
    return "/page/{}".format(page_id)


def get_menu_links():
    return [("menu {}".format(page_id), link_maker(page_id)) for page_id in DEFAULT_MENU_PAGES]

from settings.constants import DEFAULT_MENU_PAGES


def link_maker(page_id):
    return "/page/{}".format(page_id)


def get_menu_links():
    return [("menu {}".format(page_id), link_maker(page_id)) for page_id in DEFAULT_MENU_PAGES]

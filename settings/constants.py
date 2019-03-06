DATA_GEN_VOLUME = 1000
DATA_MAX_PAGES = 10000
DATA_MAX_PAGE_DEPTH = 5
DATA_MAX_LINKS_PER_PAGE = 25
DATA_MIN_LINKS_PER_PAGE = 5
DEFAULT_MENU_PAGES = [i for i in range(1, 10)]

TEMPLATE_1_CONSTANTS = {
    'kwargs': {'navbar': '/navbar/',
               'home': '/',
               'about': '/about/',
               'services': '/services/',
               'contact': '/contact/',
               },
    'menu_count': 20,
    'menu_prefix': '/page/{}/'

}
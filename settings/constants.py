DATA_GEN_VOLUME = 1000
DATA_MAX_PAGES = 10000
DATA_MAX_PAGE_DEPTH = 5

DEFAULT_MENU_PAGES = [i for i in range(1, 21)]

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
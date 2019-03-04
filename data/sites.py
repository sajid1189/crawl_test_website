import random
from settings.constants import DATA_MAX_PAGES, DEFAULT_MENU_PAGES, DATA_MAX_LINKS_PER_PAGE, DATA_MIN_PAGES_PER_PAGE


class Site(object):

    def __init__(self):
        pass

    def _gen_adjacency_sparse(self):
        """ There number of pages == DATA_MAX_PAGES. Each page will have any number of pages between DATA_MIN_PAGES_PER_PAGE
         and DATA_MAX_PAGES_PER_PAGE.
         :return a dictionary of the following structure {1: [2,3,7, 10, 9], 2: [11,2,9], ....}, where key is the page index
         and the value is a list of (indices) links on that page.

         """

        connections = dict()
        for i in range(DATA_MAX_PAGES):
            random_links = list([random.randint(1, DATA_MAX_PAGES) for _ in range(random.randint(
                DATA_MIN_PAGES_PER_PAGE, DATA_MAX_LINKS_PER_PAGE
            ))])
            random_links = list(filter(lambda x: x not in DEFAULT_MENU_PAGES, random_links))
            connections[i] = DEFAULT_MENU_PAGES + random_links
        return connections

    def new_site(self):
        connections = self._gen_adjacency_sparse()

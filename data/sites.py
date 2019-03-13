import random
import os
import sys

sys.path.append(os.path.abspath('../settings/'))
for p in sys.path:
    print(p)

from constants import DATA_MAX_PAGES, DEFAULT_MENU_PAGES, DATA_MAX_LINKS_PER_PAGE, DATA_MIN_LINKS_PER_PAGE


class Site(object):

    def __init__(self):
        pass


def gen_adjacency_sparse_default(total_pages=None, links_per_page=None):
    """ There number of pages == DATA_MAX_PAGES. Each page will have any number of pages between DATA_MIN_PAGES_PER_PAGE
     and DATA_MAX_PAGES_PER_PAGE.
     :return a dictionary of the following structure {1: [2,3,7, 10, 9], 2: [11,2,9], ....}, where key is the page index
     and the value is a list of (indices) links on that page.

     """
    total_pages = total_pages or DATA_MAX_PAGES
    links_per_page = links_per_page or DATA_MAX_LINKS_PER_PAGE
    connections = dict()
    for i in range(total_pages):
        random_links = list([random.randint(1, total_pages) for _ in range(random.randint(
            DATA_MIN_LINKS_PER_PAGE, links_per_page
        ))])
        random_links = list(filter(lambda x: x not in DEFAULT_MENU_PAGES, random_links))
        connections[i] = DEFAULT_MENU_PAGES + random_links
    return connections


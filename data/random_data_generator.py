import random
import json
import os

from settings.constants import DATA_MAX_PAGES, DEFAULT_MENU_PAGES, DATA_MAX_LINKS_PER_PAGE


def gen_adjacency_sparse():
    connections = dict()
    for i in range(DATA_MAX_PAGES):
        random_links = list([random.randint(1, DATA_MAX_PAGES) for _ in range(random.randint(5, DATA_MAX_LINKS_PER_PAGE))])
        random_links = list(filter(lambda x: x not in DEFAULT_MENU_PAGES, random_links))
        connections[i] = DEFAULT_MENU_PAGES + random_links
    return connections


if __name__ == '__main__':
    gen_adjacency_sparse()
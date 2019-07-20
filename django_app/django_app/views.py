import random
import os
import sys
from django.views.generic import TemplateView
from django.contrib import messages

sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('../../settings/'))

from utils.links import link_maker, get_menu_links
from.models import *
from constants import DATA_MAX_PAGES, DEFAULT_MENU_PAGES, DATA_MAX_LINKS_PER_PAGE, DATA_MIN_LINKS_PER_PAGE


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        first_page = PageStructure.objects.filter(site=Site.objects.filter(current=True).first()).first()
        context = super(Home, self).get_context_data(**kwargs)
        current_site = Site.objects.filter(current=True).first()

        context.update({
            'page': link_maker(first_page.id),
            'min_links': DATA_MIN_LINKS_PER_PAGE,
            'max_links': current_site.links_per_page,
            'total_pages': current_site.total_pages
        })
        return context


class Page(TemplateView):
    template_name = 'template1.html'
    
    def get_context_data(self, **kwargs):
        page_index = kwargs.get('page_index')
        current_site = Site.objects.filter(current=True).first()
        context = super(Page, self).get_context_data(**kwargs)
        if not current_site:
            messages.add_message(self.request, messages.ERROR, "Set the current site")
            return context
        ps = PageStructure.objects.get(site=current_site, page=page_index)
        links = json.loads(ps.links)

        links = [("page {}".format(link), link_maker(link)) for link in links]

        context.update(
            {
                'links': links,
                'menu_items': get_menu_links(),
                'lorem_count': [i for i in range(1, (page_index % 50) + 1)]
            }
        )
        return context

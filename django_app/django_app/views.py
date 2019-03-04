from django.http import HttpResponse
from django.views.generic import TemplateView
from settings.constants import *

from.models import *


class Home(TemplateView):
    template_name = 'home.html'


class Page(TemplateView):
    template_name = 'template1.html'
    
    def get_context_data(self, **kwargs):
        page_index = kwargs.get('page_index')
        current_site = Site.objects.filter(current=True).first()
        if not current_site:
            return HttpResponse("Set the current site first")
        ps = PageStructure.objects.get(site=current_site, page=page_index)
        links = json.loads(ps.links)
        context = super(Page, self).get_context_data(**kwargs)

        links = [("page {}".format(link), "/page/{}".format(link)) for link in links]
        menu_items = [("menu {}".format(menu_item), "/page/{}".format(menu_item)) for menu_item in DEFAULT_MENU_PAGES]
        context.update(
            {
                'links': links,
                'menu_items': menu_items
            }
        )
        return context

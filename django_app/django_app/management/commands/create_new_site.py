import json

from django.core.management.base import BaseCommand, CommandError

from django_app.models import Site, PageStructure
from data.sites import gen_adjacency_sparse_default

class Command(BaseCommand):
    help = 'Creates a new site with the given page size and links per page.'

    def add_arguments(self, parser):
        parser.add_argument('sizes', nargs='+', type=int)

    def handle(self, *args, **options):
        total_pages = options['sizes'][0]
        kwargs = {'total_pages': total_pages}
        links_per_page = options['sizes'][1] if len(options['sizes']) > 1 else None
        if links_per_page:
            if links_per_page > total_pages:
                raise ValueError("links per page cannot be greater than the number of pages.")
            kwargs.update({'links_per_page': links_per_page})
        site = Site.objects.create(**kwargs)
        Site.objects.all().update(current=False)
        site.current = True
        site.save()

        connections = gen_adjacency_sparse_default(total_pages=total_pages, links_per_page=links_per_page)

        for page_index, links in connections.items():
            PageStructure.objects.create(
                page=page_index,
                links=json.dumps(links),
                site=site
            )

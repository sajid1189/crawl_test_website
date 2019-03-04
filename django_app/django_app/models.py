import json

from django.db import models


class Site(models.Model):
    total_pages = models.IntegerField()
    links_per_page = models.SmallIntegerField(default=15)
    description = models.TextField(null=True, blank=True)
    current = models.BooleanField(default=False)
    # TODO make sure only one site is set current


class PageStructure(models.Model):
    page = models.IntegerField(db_index=True)
    links = models.TextField(null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('page', 'site')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.pk:
            try:
                json.loads(self.links)
            except json.decoder.JSONDecodeError:
                self.links = json.dumps([])
        return super(PageStructure, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )


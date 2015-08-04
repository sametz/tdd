from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)  # although P214 test passed, slapping P215 solution in anyways
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text  # Although p214 test passed, this seems useful to add anyways (p215)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Notes(models.Model):
    post_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return 'Note #{}'.format(self.id)

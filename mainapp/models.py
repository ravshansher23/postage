# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True, null=False)
    first_name = models.CharField(max_length=256, verbose_name="First_name")
    last_name = models.CharField(max_length=256, verbose_name="Last_name")
    birthday = models.DateField(verbose_name="Birthday", null=False)
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)



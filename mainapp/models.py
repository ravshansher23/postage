# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Followers(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True, null=False)
    first_name = models.CharField(max_length=256, verbose_name="First_name")
    last_name = models.CharField(max_length=256, verbose_name="Last_name")
    birthday = models.DateField(verbose_name="Birthday", null=False)
    is_open = models.BooleanField(verbose_name="is_open", default=False)

    def __str__(self):
        return self.email

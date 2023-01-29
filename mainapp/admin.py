# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mainapp import models as mainapp_models


@admin.register(mainapp_models.Followers)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name", "email"]
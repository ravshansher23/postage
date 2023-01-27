# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import FileResponse, JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from mainapp import models as mainapp_models
from mainapp import tasks as mainapp_tasks


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"
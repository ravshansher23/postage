# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from mainapp import models as mainapp_models
from mainapp import tasks as mainapp_tasks
from mainapp import forms as mainapp_forms



class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["form"] = mainapp_forms.MailForm()
        context["followers"] = mainapp_models.Followers.objects.all()
        return context

    def post(self, *args, **kwargs):
        name = mainapp_models.Followers.objects.all()
        for item in name:
            obj = mainapp_models.Followers.objects.get(pk=item.pk)
            email = obj.email
            names = obj.first_name
            mainapp_tasks.send_email.delay(
                {
                    "name": names,
                    "email": email

                }
            )
        return HttpResponseRedirect(reverse_lazy("mainapp:main_page"))    
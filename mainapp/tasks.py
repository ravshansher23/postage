from __future__ import absolute_import, unicode_literals
from typing import Dict
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string
from mainapp import models as mainapp_models
from django.utils.html import strip_tags
from django.http import request
from django.urls import reverse
from django.http import HttpRequest

@shared_task
def send_email(messege_form):
    html_template_path = 'email_templates/mail.html'
    requests = HttpRequest()
    location = "mainapp:image_load"
    url = requests.get_full_path(reverse(location))
    context_data = {'name': messege_form['name'], 'image_url': url}
    email_html = get_template(html_template_path).render(context_data)
    email_html_template = strip_tags(email_html)
    receiver_email = messege_form["email"]
    email_msg = send_mail(
        'Test mail',
        email_html_template,
        'ravsh@ru.ru',
        [receiver_email],
        fail_silently=False,      
    )
    return None

send_email.__annotations__ = Dict[str, str]


@shared_task
def send_email_15():
    name = mainapp_models.Followers.objects.all()
    html_template_path = 'email_templates/mail.html'
    for item in name:
        obj = mainapp_models.Followers.objects.get(pk=item.pk)
        email = obj.email
        names = obj.first_name  
        
        requests = HttpRequest()
        location = "mainapp:image_load"
        url = requests.get_full_path(reverse(location))
        context_data = {'name': names, 'image_url': url}
        email_html = get_template(html_template_path).render(context_data)
        email_html_template = strip_tags(email_html)
        receiver_email = email
        email_msg = send_mail(
            'Test mail',
            email_html_template,
            'ravsh@ru.ru',
            [receiver_email],
            fail_silently=False,      
        )
    return None
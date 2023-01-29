import logging

from typing import Dict, Union
from mainapp import models as mainapp_models
from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from config import settings


@shared_task
def send_email(messege_form):
    html_template_path = 'email_templates/mail.html'
    context_data = {'name': messege_form["name"]}
    email_html_template = get_template(html_template_path).render(context_data)
    receiver_email = messege_form["email"]
    email_msg = send_mail(
        'Test mail',
        email_html_template,
        'ravsh@ru.ru',
        [receiver_email],
        fail_silently=False
    )
    return None

send_email.__annotations__ = Dict[str, str]
from typing import Dict
from celery import shared_task
from celery.schedules import crontab
from django.core.mail import send_mail
from django.template.loader import get_template
from mainapp import models as mainapp_models


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
    
        context_data = {'name': names}
        email_html_template = get_template(html_template_path).render(context_data)
        receiver_email = email
        email_msg = send_mail(
            'Test mail',
            email_html_template,
            'ravsh@ru.ru',
            [receiver_email],
            fail_silently=False,      
        )
    return None

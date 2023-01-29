from django.conf.urls import url
from mainapp import views

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    url("", views.MainPageView.as_view(), name="main_page"),


]
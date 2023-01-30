import debug_toolbar
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", RedirectView.as_view(url="mainapp/")),
    url("mainapp/", include("mainapp.urls", namespace="mainapp")),
# r'^posts/$'
]


if settings.DEBUG:
    urlpatterns.append(url("__debug__/", include(debug_toolbar.urls)))
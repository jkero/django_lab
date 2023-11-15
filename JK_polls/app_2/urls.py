from django.views.generic import RedirectView

app_name = "app_2"

from django.urls import path

from . import views

app_name = "app_2"
urlpatterns = [
    path("", views.index, name="index"),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path("create/", views.create_note, name="create"),
]
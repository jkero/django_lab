from django.urls import path

from archive import views

urlpatterns = [
    path("", views.index, name="index"),
]
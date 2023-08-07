from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name = 'webapp-home'),
    path("search/", views.search, name = 'webapp-search'),
    path("", views.base, name = 'webapp-base'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_quote, name="add_quote"),
    path("quotes/", views.quote_list, name="quote_list"),
]

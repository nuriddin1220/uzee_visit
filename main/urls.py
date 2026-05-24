from django.urls import path
from .views import home,root_redirect,contact

urlpatterns = [
    path("", root_redirect),
    path("<str:lang>/", home, name="home_lang"),
    path("<str:lang>/contact/", contact, name="contact"),
]
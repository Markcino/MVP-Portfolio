from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('do_login', views.do_login, name="do_login"),
    path('do_logout', views.do_logout, name="do_logout"),
]

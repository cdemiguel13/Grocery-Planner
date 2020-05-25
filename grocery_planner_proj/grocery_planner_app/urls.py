from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path("register", views.register),
    path("logout", views.logout),
    path("success", views.success),
    path("login", views.login),
]

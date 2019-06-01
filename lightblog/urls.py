from django.urls import path
from . import views

urlpatterns = [
    path('', views.lightblog_list, name="lightblog_list"),
]
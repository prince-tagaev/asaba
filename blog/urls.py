from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='home'),
]

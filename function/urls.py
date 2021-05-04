from django.urls import path
from . import views

app_name= 'function'
urlpatterns = [
    path('contact', views.contact, name='contact'),
]
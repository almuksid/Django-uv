from django.urls import path
from .import views

app_name = 'day2'

urlpatterns = [
    path('dhaka/', views.dhaka, name='dhaka'),
    path('rajshahi/', views.rajshahi, name='rajshahi'),
]

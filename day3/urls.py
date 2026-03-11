from django.urls import path
from .import views


app_name = 'day3'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('submission_handler/', views.submission_handler, name='submission_handler'),
    # path('messages/', views.messages, name='messages'),
]

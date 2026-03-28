from django.urls import path
from . import views
app_name = 'day4'

# Rout parten
urlpatterns = [
    path('check/<int:number>/', views.number, name="number-even-odd"),
    path('record/<str:name>/<int:age>/', views.record, name="record"),
    path('users/', views.UserViews.as_view(), name='users'),
    path('users/<int:id>/', views.UserDetailsView.as_view(), name="user"),
    path('jsonusers/', views.json_users, name="json-users"),
    path('jsonusers/<int:userId>/', views.json_single_users, name="json-single-users")

]


# GET, POST, PUT, PATCH, DELETE

# Resource collection
# users/ GET, POST
# users/1 GET, PUT, PATCH, DELETE
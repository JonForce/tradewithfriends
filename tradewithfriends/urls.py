from django.contrib import admin
from django.urls import path
from tradewithfriends.views import view_profile, login

urlpatterns = [
    path('/login', login),
    path('<str:username>/', view_profile),
    path('', view_profile),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('function/', include('vote_rate.urls')),
]

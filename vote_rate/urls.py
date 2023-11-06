from django.contrib import admin
from django.urls import path, include
from vote_rate import views

urlpatterns = [
    path('rate/<str:name>', views.CandidateAPI),
]

from django.urls import path
from vote_rate import views

urlpatterns = [
    path('all', views.ALLCandidateAPI),
    path('rate/<str:name>', views.CandidateAPI),
    
]

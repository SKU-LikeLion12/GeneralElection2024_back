from django.urls import path
from vote_rate import views

urlpatterns = [
    path('rate/', views.ALLCandidateAPI),
    path('refresh/', views.RefreshAPI),
    
]

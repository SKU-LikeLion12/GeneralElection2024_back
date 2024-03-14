from django.urls import path
from vote_rate import views

urlpatterns = [
    # 2024 본선거
    path('rate/', views.ALLCandidateAPI),
    path('refresh/', views.RefreshAPI),
    
    # 2024 보궐선거
    path('by-election/rate/', views.ByElectionALLCandidateAPI),
    path('by-election/refresh/', views.ByElectionRefreshAPI)
    
]

from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sports', SportList.as_view(), name='sports'),
    path('leagues', LeagueList.as_view(), name='leagues'),
    path('teams', TeamList.as_view(), name='teams'),
    path('matches', MatchList.as_view(), name='matches'),
    path('leagues/<int:pk>/teams/', LeagueTeamsView.as_view(), name='league-teams'),
    path('teams/<int:pk>/matches/', TeamMatchesView.as_view(), name='team-matches'),
]
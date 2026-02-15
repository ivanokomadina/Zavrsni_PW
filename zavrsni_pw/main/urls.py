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
    path('teams/add', TeamCreateView.as_view(), name='team-add'),
    path('teams/<int:pk>/update', TeamUpdateView.as_view(), name='team-update'),
    path('teams/<int:pk>/delete', TeamDeleteView.as_view(), name='team-delete'),
    path('matches/add', MatchCreateView.as_view(), name='match-add'),
    path('matches/<int:pk>/update', MatchUpdateView.as_view(), name='match-update'),
    path('matches/<int:pk>/delete', MatchDeleteView.as_view(), name='match-delete'),
]
from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sports', SportList.as_view(), name='sports'),
    path('leagues', LeagueList.as_view(), name='leagues'),
    path('teams', TeamList.as_view(), name='teams'),
    path('matches', MatchList.as_view(), name='matches')
]
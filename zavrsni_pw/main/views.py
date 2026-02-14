from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from main.models import *

class HomeView(TemplateView):
    template_name = "main/home.html"

class SportList(ListView):
    model = Sport

class LeagueList(ListView):
    model = League

class TeamList(ListView):
    model = Team

class MatchList(ListView):
    model = Match
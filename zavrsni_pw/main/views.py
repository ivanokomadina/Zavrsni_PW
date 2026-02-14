from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from main.models import *
from django.db.models import Q

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

class LeagueTeamsView(ListView):
    model = Team
    template_name = 'main/league_teams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        self.league = get_object_or_404(League, pk=self.kwargs['pk'])
        return Team.objects.filter(league=self.league)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['league'] = self.league
        return context
    
class TeamMatchesView(ListView):
    model = Match
    template_name = 'main/team_matches.html'
    context_object_name = 'matches'

    def get_queryset(self):
        self.team = get_object_or_404(Team, pk=self.kwargs['pk'])
        return Match.objects.filter(
            Q(home_team=self.team) | Q(away_team=self.team)
        ).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = self.team
        return context
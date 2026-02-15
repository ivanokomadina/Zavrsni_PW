from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from main.models import *
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import TeamForm, MatchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = "main/home.html"


class SportList(ListView):
    model = Sport


class LeagueList(ListView):
    model = League

    def get_queryset(self):
        queryset = League.objects.all()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class TeamList(ListView):
    model = Team

    def get_queryset(self):
        queryset = Team.objects.all()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'main/team_form.html'
    success_url = reverse_lazy('main:teams')


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'main/team_form.html'
    success_url = reverse_lazy('main:teams')


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = 'main/team_confirm_delete.html'
    success_url = reverse_lazy('main:teams')


class MatchList(ListView):
    model = Match
    ordering = ['-date']

    def get_queryset(self):
        queryset = Match.objects.all()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                home_team__name__icontains=search
            ) | queryset.filter(
                away_team__name__icontains=search
            )

        return queryset


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'main/match_form.html'
    success_url = reverse_lazy('main:matches')


class MatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'main/match_form.html'
    success_url = reverse_lazy('main:matches')


class MatchDeleteView(LoginRequiredMixin, DeleteView):
    model = Match
    template_name = 'main/match_confirm_delete.html'
    success_url = reverse_lazy('main:matches')


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


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

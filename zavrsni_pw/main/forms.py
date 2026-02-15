from django import forms
from .models import Team, Match

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'league', 'founded_year']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            'league',
            'home_team',
            'away_team',
            'date',
            'home_score',
            'away_score'
        ]
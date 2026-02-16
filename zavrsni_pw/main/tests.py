from django.test import TestCase
from django.urls import reverse
from django.db.models import Q
from main.factory import SportFactory, LeagueFactory, TeamFactory, MatchFactory

# Create your tests here.

class ModelTests(TestCase):

    def test_create_sport(self):
        sport = SportFactory()
        self.assertIsNotNone(sport.id)

    def test_team_has_league(self):
        team = TeamFactory()
        self.assertIsNotNone(team.league)

class LeagueTeamsViewTest(TestCase):

    def test_league_shows_only_its_teams(self):
        league1 = LeagueFactory()
        league2 = LeagueFactory()

        team1 = TeamFactory(league=league1)
        team2 = TeamFactory(league=league2)

        response = self.client.get(
            reverse('main:league-teams', args=[league1.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, team1.name)
        self.assertNotContains(response, team2.name)

class TeamMatchesViewTest(TestCase):

    def test_team_shows_home_and_away_matches(self):
        team = TeamFactory()

        home_match = MatchFactory(home_team=team)
        away_match = MatchFactory(away_team=team)

        other_match = MatchFactory()

        url = reverse('main:team-matches', args=[team.id])
        response = self.client.get(url)

        self.assertContains(response, home_match.home_team.name)
        self.assertContains(response, away_match.away_team.name)
        self.assertNotContains(response, other_match.home_team.name)

class UrlTests(TestCase):

    def test_home_page(self):
        self.assertEqual(
            self.client.get(reverse('main:home')).status_code,
            200
        )

    def test_sports_page(self):
        self.assertEqual(
            self.client.get(reverse('main:sports')).status_code,
            200
        )

    def test_leagues_page(self):
        self.assertEqual(
            self.client.get(reverse('main:leagues')).status_code,
            200
        )

    def test_teams_page(self):
        self.assertEqual(
            self.client.get(reverse('main:teams')).status_code,
            200
        )

    def test_matches_page(self):
        self.assertEqual(
            self.client.get(reverse('main:matches')).status_code,
            200
        )

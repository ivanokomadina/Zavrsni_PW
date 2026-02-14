import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Sport, League, Team, Match
from main.factory import SportFactory, LeagueFactory, TeamFactory, MatchFactory


NUM_SPORTS = 5
NUM_LEAGUES = 25
NUM_TEAMS = 100
NUM_MATCHES = 200


class Command(BaseCommand):
    help = "Generates controlled test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")

        for model in [Match, Team, League, Sport]:
            model.objects.all().delete()

        self.stdout.write("Creating sports...")
        sports = SportFactory.create_batch(NUM_SPORTS)

        self.stdout.write("Creating leagues...")
        leagues = [
            LeagueFactory.create(
                sport=random.choice(sports)
            )
            for _ in range(NUM_LEAGUES)
        ]

        self.stdout.write("Creating teams...")
        teams = [
            TeamFactory.create(
                league=random.choice(leagues)
            )
            for _ in range(NUM_TEAMS)
        ]

        self.stdout.write("Creating matches...")
        for _ in range(NUM_MATCHES):
            league = random.choice(leagues)
            league_teams = [t for t in teams if t.league == league]

            if len(league_teams) < 2:
                continue

            home_team, away_team = random.sample(league_teams, 2)

            MatchFactory.create(
                league=league,
                home_team=home_team,
                away_team=away_team
            )

        self.stdout.write(
            self.style.SUCCESS("Test data successfully generated!")
        )

import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory

class SportFactory(DjangoModelFactory):
    class Meta:
        model = Sport

    name = factory.Faker("word")
    description = factory.Faker("sentence", nb_words=20)

class LeagueFactory(DjangoModelFactory):
    class Meta:
        model = League

    name = factory.Faker("company")
    country = factory.Faker("country")
    sport = factory.SubFactory(SportFactory)

class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Faker("first_name")
    league = factory.SubFactory(LeagueFactory)
    founded_year = factory.Faker("random_int", min=1850, max=2024)

class MatchFactory(DjangoModelFactory):
    class Meta:
        model = Match

    league = factory.SubFactory(LeagueFactory)
    home_team = factory.SubFactory(
        TeamFactory,
        league=factory.SelfAttribute("..league")
    )
    away_team = factory.SubFactory(
        TeamFactory,
        league=factory.SelfAttribute("..league")
    )
    date = factory.Faker("date_time")
    home_score = factory.Faker("random_int", min=0, max=10)
    away_score = factory.Faker("random_int", min=0, max=10)

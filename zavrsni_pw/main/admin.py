from django.contrib import admin
from .models import *

models_list = [Sport, League, Team, Match]

# Register your models here.

admin.site.register(models_list)
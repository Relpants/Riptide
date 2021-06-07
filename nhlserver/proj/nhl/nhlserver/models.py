from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=200,primary_key=True,unique=True)
	score = models.IntegerField(default = 0)
	#goalie = models.CharField(maxLenght=200)



class Game(models.Model):
	away_team = models.ForeignKey(Team, related_name = 'away_team_data',on_delete=models.CASCADE)
	home_team = models.ForeignKey(Team, related_name = 'home_team_data',on_delete=models.CASCADE)
	score = models.IntegerField(default = 0)
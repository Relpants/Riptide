from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=200,primary_key=True,unique=True,default='default')


class Date(models.Model):
	gdate = models.CharField(max_length=200,primary_key=True,default='default')

class Game(models.Model):
	game_date = models.ForeignKey(Date, related_name = 'date',on_delete=models.CASCADE)
	away_team = models.ForeignKey(Team, related_name = 'away_team_data',on_delete=models.CASCADE)
	home_team = models.ForeignKey(Team, related_name = 'home_team_data',on_delete=models.CASCADE)
	away_team_score = models.IntegerField(default=0)
	home_team_score = models.IntegerField(default=0)
	away_team_goalie = models.CharField(max_length=200,blank=True)
	home_team_goalie = models.CharField(max_length=200,blank=True)
	away_team_goalie_sv = models.IntegerField(default=0)
	home_team_goalie_sv = models.IntegerField(default=0)


class Meta:
    unique_together = ('home_team', 'away_team', 'game_date')
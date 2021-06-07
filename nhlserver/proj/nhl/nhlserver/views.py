from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
# Create your views here.
from nhlserver.models import *

def index(request):
	date = '20191028'
	# if we have date display models

	resp = requests.get('https://site.web.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?region=us&lang=en&contentorigin=espn&limit=100&calendartype=blacklist&includeModules=videos%2Ccards&dates='+date+'&buyWindow=1m&showAirings=buy%2Clive&showZipLookup=true')
	resp = json.dumps(resp.json(), sort_keys=True, indent=4)
	r = json.loads(resp)
	num_of_games = r["events"]
	i = 0

	while (i < len(num_of_games)):
		game = r["events"][i]
		game_stats = game["competitions"][0] 
		home_team_info = game_stats["competitors"][0]
		home = Team.objects.get_or_create(name = home_team_info["team"]["displayName"],
							score = home_team_info["score"])
		if(home[1] == False):
			home = Team.objects.all().filter(name = home_team_info["team"]["displayName"]).filter(score = home_team_info["score"])

		
		away_team_info = game_stats["competitors"][1]
		away = Team.objects.get_or_create(name = away_team_info["team"]["displayName"],
							score = home_team_info["score"])
		if(away[1] == False):
			away = Team.objects.all().filter(name = away_team_info["team"]["displayName"]).filter(score = home_team_info["score"])
		game_data = Game.objects.get_or_create(away_team = away[0],home_team = home[0])
		i = i + 1


	games_list = Game.objects.all()
	context = {'games_list' : games_list}
	template = loader.get_template('nhlserver/scoreboard.html')
	return HttpResponse(template.render(context, request))
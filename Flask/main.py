from flask import Flask, render_template
from team import Team
import requests
import json

app = Flask(__name__)



@app.route("/scores")
def scores():
	date = '20200209'
	r = make_request(date)


	num_of_games = r["events"]
	i = 0

	home_team_list = []
	away_team_list = []

	while(i < len(num_of_games)):

		home_team = Team()
		away_team = Team()
		game = r["events"][i]
		game_stats = game["competitions"][0]

		home_team_info = game["competitions"][0]["competitors"][0]
		home_team.setName(home_team_info["team"]["displayName"])
		home_team.setLogo(home_team_info["team"]["logo"])
		home_team.setScore(home_team_info["score"])

		away_team_info = game["competitions"][0]["competitors"][1]
		away_team.setName(away_team_info["team"]["displayName"])
		away_team.setLogo(away_team_info["team"]["logo"]) 
		away_team.setScore(away_team_info["score"]) 

		if(home_team_info["winner"] == True and (game_stats["status"]["featuredAthletes"][0]["athlete"]["team"]["id"] == home_team_info["team"]["id"])):
			home_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][0]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][0]["statistics"][6]["displayValue"])
			away_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][1]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][1]["statistics"][6]["displayValue"])
		else:
			home_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][1]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][1]["statistics"][6]["displayValue"])
			away_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][0]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][0]["statistics"][6]["displayValue"])
		
		home_team_list.append(home_team)
		away_team_list.append(away_team)

		i = i + 1

	print(len(home_team_list))


	return render_template('template.html', data=home_team_list)


@app.route("/")
def home():
	return "Hello, World"

def make_request(date):
	resp = requests.get('https://site.web.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?region=us&lang=en&contentorigin=espn&limit=100&calendartype=blacklist&includeModules=videos%2Ccards&dates='+date+'&buyWindow=1m&showAirings=buy%2Clive&showZipLookup=true')
	resp = json.dumps(resp.json(), sort_keys=True, indent=4)
	r = json.loads(resp)
	return r

if __name__ == "__main__":
	app.run(debug=True)



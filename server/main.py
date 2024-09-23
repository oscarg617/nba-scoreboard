import flask
import random
from flask import Flask
from flask_cors import CORS
from nba_api.stats.endpoints import leagueleaders
from  nba_api.live.nba.endpoints import scoreboard

app = Flask(__name__)
CORS(app)

colors = {
    "ATL": ["#c8102e", "#ffffff"],
    "BKN": ["#010101", "#ffffff"],
    "BOS": ["#007a33", "#ffffff"],
    "CHA": ["#201747", "#00778b"],
    "CHI": ["#ba0c2f", "#000000"],
    "CLE": ["#6f263d", "#041e42"],
    "DAL": ["#0050b5", "#8d9093"],
    "DEN": ["#418fde", "#ffc72c"],
    "DET": ["#003da5", "#d50032"],
    "GSW": ["#ffc72d", "#003da5"],
    "HOU": ["#ba0c2f", "#8d9093"],
    "IND": ["#041e42", "#ffb81c"],
    "LAC": ["#d50032", "#003da5"],
    "LAL": ["#702f8a", "#ffc72c"],
    "MEM": ["#23375b", "#6189b9"],
    "MIA": ["#862633", "#000000"],
    "MIL": ["#2c5234", "#ddcba4"],
    "MIN": ["#002b5c", "#c6cfd4"],
    "NOP": ["#002b5c", "#b4975a"],
    "NYK": ["#003da5", "#ff671f"],
    "OKC": ["#007dc3", "#f05133"],
    "ORL": ["#007dc5", "#c4ced3"],
    "PHI": ["#006bb6", "#ed174c"],
    "PHX": ["#e56020", "#1d1160"],
    "POR": ["#f0163a", "#000000"],
    "SAC": ["#724c9f", "#8e9090"],
    "SAS": ["#b6bfbf", "#000000"],
    "TOR": ["#ce1141", "#c4ced3"],
    "UTA": ["#002b5c", "#f9a01b"],
    "WAS": ["#0c2340", "#c8102e"]
}

@app.route("/today")
def scoreboard_today():
    # Today's Score Board
    games = scoreboard.ScoreBoard()

    # json
    games.get_json()

    # dictionary
    res = games.get_dict()

    games_dicts = []
    games = res["scoreboard"]["games"]
    for game in games:
        gameStatusText = game["gameStatusText"]
        split = gameStatusText.split()

        homeTeam = game["homeTeam"]
        awayTeam = game["awayTeam"]
        homeTeamName = homeTeam["teamTricode"]
        awayTeamName = awayTeam["teamTricode"]

        if split[0] == "Half":
            status = "LIVE"
            statusColor = "red"
            quarter = "Halftime"
            time = "0:00"

        elif split[0] == 'END':
            status = "LIVE"
            statusColor = "red"
            quarter = split[1]
            time = "0:00"

        elif len(split) == 3:
            status = split[0] + split[1] + " " + split[2]
            statusColor = "orange"
            quarter = ""
            time = ""
        elif len(split) == 2:
            status = "LIVE"
            statusColor = "red"
            quarter = split[0]
            time = split[1]
        else:
            status = "FINAL"
            statusColor = "yellow"
            quarter = ""
            time = ""

        game_dict = {
            "poRoundDesc": game["poRoundDesc"],
            "seriesGameNumber": game["seriesGameNumber"],
            "seriesText": game["seriesText"],
            "homeTeam": homeTeamName,
            "homeScore": homeTeam["score"],
            "awayTeam": awayTeamName,
            "awayScore": awayTeam["score"],
            "quarter": quarter,
            "status": status,
            "statusColor": statusColor,
            "time": time,
            "homeColor1": colors[homeTeamName][0],
            "homeColor2": colors[homeTeamName][1],
            "awayColor1": colors[awayTeamName][0],
            "awayColor2": colors[awayTeamName][1],
        }
        games_dicts.append(game_dict)

    response = flask.jsonify(games_dicts)
    return response

@app.route("/random")
def random_player():
    leaders = leagueleaders.LeagueLeaders(season_type_all_star="Playoffs")

    json = leaders.get_json()

    dict = leaders.get_dict()

    players = dict["resultSet"]["rowSet"]
    
    index = random.randint(0, 100)
    player = players[index]

    player_dict = {
        "name": player[2],
        "teamAbbr": player[4],
        "ppg": str(round(player[-4] / player[5], 1)) + " PPG",
        "rpg": str(round(player[-10] / player[5], 1)) + " RPG",
        "apg": str(round(player[-9] / player[5], 1)) + " APG",
        "fgp": str(round(player[9] * 100, 1)) + " FG%",
        "threep": str(round(player[12] * 100, 1)) + " 3PT%",
        "ftp": str(round(player[15] * 100, 1)) + " FT%",
        "headshot": "https://cdn.nba.com/headshots/nba/latest/1040x760/" + str(player[0]) + ".png",
        "teamColor1": colors[player[4]][0],
        "teamColor2": colors[player[4]][1],
    }


    response = flask.jsonify(player_dict)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
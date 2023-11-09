import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []
        self.get_players()

    def get_players(self):
        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)

    def __iter__(self):
        return iter(self.players)

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        filtered = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(filtered, key=lambda player: player.goals + player.assists, reverse=True)





def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    for player in players:
        print(player)

main()
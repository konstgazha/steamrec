import requests
from bs4 import BeautifulSoup

key = ''

def get_player_info(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s'
    player = requests.get(url % (key, steamid)).json()
    return player

def get_app_info(appid):
    url = 'http://store.steampowered.com/api/appdetails?appids=%s&cc=ee&l=english'
    app = requests.get(url % (appid)).json()
    return app

def get_owned_games(steamid):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json'
    owned_games = requests.get(url % (key, steamid)).json()
    return owned_games

def get_group_info(group, page):
    url = 'http://steamcommunity.com/groups/%s/memberslistxml/?xml=1&p=%s'
    response = requests.get(url % (group, page)).text
    soup = BeautifulSoup(response, 'html5lib')
    return soup

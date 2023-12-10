import requests
from logger import logger

def get_chuck_noris_joke():
    url = f"https://api.chucknorris.io/jokes/random"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['value']
    else:
        logger.error(f"Error: Unable to fetch game info. Status code: {response.status_code}")
        return None
    

def get_games_data(game_title):
    url = f"https://www.cheapshark.com/api/1.0/games?title={game_title}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        logger.error(f"Error: Unable to fetch game info. Status code: {response.status_code}")
        return None
    
def get_games_prices(data):
    game_list = []
    for game_data in data:
        game_name = game_data["external"]
        game_price = game_data["cheapest"]
        game_list.append(f"{game_name}: ${game_price}")
    return game_list
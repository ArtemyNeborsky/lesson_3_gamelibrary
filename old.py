import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("TOKEN")


def get_games(api):
    payload = {"key": api_key, "genres": "strategy", "metacritic": 100, "tags": "multiplayer"}
    url = "https://api.rawg.io/api/games"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    games_dict = []
    for num in range(10):
        game_name = response.json()["results"][num]["name"]
        game_date = response.json()["results"][num]["released"]
        game_link = f"https://rawg.io/games/{response.json()["results"][num]["slug"]}"
        game_screenshots = ""
        for x in range(len(response.json()["results"][num]["short_screenshots"])):
            game_screenshot = response.json()["results"][num]["short_screenshots"][x]["image"]
            game_screenshots = game_screenshots + f" {game_screenshot}\n"
        game_stores = ""
        game = {
            "name": game_name,
            "date": game_date,
            "link": game_link,
            "screenshots": game_screenshots,
            "stores": game_stores
        }
        games_dict.append(game)
    return games_dict


def main():
    for numb in range(len(get_games(api_key))):
        print("Название игры:", get_games(api_key)[numb]["name"])
        print("Дата выхода:", get_games(api_key)[numb]["date"])
        print("Ссылка на игру:", get_games(api_key)[numb]["link"])
        print("Магазины: -")
        print("Скриншоты:", get_games(api_key)[numb]["screenshots"])


if __name__ == "__main__":
    main()
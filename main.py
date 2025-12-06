import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOKEN")


def get_games_list():
    params = {
        "key": api_key,
        "genres": "strategy",
        "tags": "multiplayer",
        "metacritic": "80,100",
        "page_size": 10
    }
    response = requests.get("https://api.rawg.io/api/games", params=params)
    return response.json()["results"]


def get_game_screenshots(game):
    screenshots = []
    for screenshot in game.get("short_screenshots"):
        screenshots.append(screenshot["image"])
    return screenshots


def get_stores_for_game(game_id):
    url = f"https://api.rawg.io/api/games/{game_id}/stores"
    params = {"key": api_key}

    response = requests.get(url, params=params)
    stores = response.json()["results"]

    store_list = []
    for store in stores:
        store_list.append(f"{store['url']}")
    return "\n".join(store_list)


def main():
    games_data = get_games_list()
    for game in games_data:
        screenshots = get_game_screenshots(game)
        stores = get_stores_for_game(game["id"])

        print(f"\nИгра: {game['name']}")
        print(f"Дата выхода: {game['released']}")
        print(f"Ссылка: https://rawg.io/games/{game['slug']}")
        print("Скриншоты из игры:")
        for screenshot in screenshots:
            print(f"{screenshot}")
        print(f"Где купить:\n{stores}")


if __name__ == "__main__":
    main()
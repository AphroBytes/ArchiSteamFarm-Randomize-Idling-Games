import json
import os
import random
import time
from steam.webapi import WebAPI

from ASFConfig import ASFConfig

# load this tool config
with open('config.json') as f:
    TOOL_CONFIG = json.load(f)
PATH_TO_ASF_CONFIG_FILE = os.path.join(os.path.dirname(__file__), TOOL_CONFIG['configFile'])
PATH_TO_OWNED_GAMES_DATA = os.path.join(os.path.dirname(__file__), TOOL_CONFIG['ownedGames'])
STEAM_API_KEY = TOOL_CONFIG['steamKey']
STEAM_ID = TOOL_CONFIG['steamIds']
REFRESH_TIME = TOOL_CONFIG['refreshTime']


def main():
    # check whether ASF config is there
    if os.path.exists(PATH_TO_ASF_CONFIG_FILE):
        ASF_config = ASFConfig(PATH_TO_ASF_CONFIG_FILE)
        api = WebAPI(key=STEAM_API_KEY)
        # print(api.ISteamUser.GetPlayerSummaries(steamids=steam_id))

        # if the ownedGames.json is not there, create and cache it
        if not os.path.exists(PATH_TO_OWNED_GAMES_DATA):
            print("ownedGames.json does not exist. Creating new file ...")
            owned_games_data = api.IPlayerService.GetOwnedGames(steamid=STEAM_ID,
                                                                include_appinfo=True,
                                                                include_played_free_games=False,
                                                                appids_filter=[],
                                                                include_free_sub=False)
            with open(PATH_TO_OWNED_GAMES_DATA, 'w') as outfile:
                json.dump(owned_games_data, outfile, sort_keys=True, indent=4)
        else:
            print("Reading data from OwnedGames.json")
            with open(PATH_TO_OWNED_GAMES_DATA) as f2:
                owned_games_data = json.load(f2)

        # get random 32 games
        random_games_list = random.sample(owned_games_data['response']['games'], 32)

        # get random 32 appids
        random_appid_list = []
        print("\nList of games that will be idling:")
        for random_game in random_games_list:
            random_appid_list.append(random_game['appid'])
            print(str(random_game['appid']) + ": " + random_game['name'])

        ASF_config.update_GamesPlayedWhileIdle(random_appid_list)

    else:
        print("Path to the ASF config file is not valid, please quit and change config.json")
        print("Current path: " + PATH_TO_ASF_CONFIG_FILE)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print("List will randomize again in : " + timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('\n\n\n')


if __name__ == "__main__":
    try:
        while True:
            main()
            print("\n")
            countdown(REFRESH_TIME)

    except KeyboardInterrupt:
        pass

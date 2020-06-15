# ArchiSteamFarm-Randomize-Idling-Games

Currently, there is a field in ASF called "GamesPlayedWhileIdle" in which you can put in up to 32 games (appid) to idle and farm the hours from. However, the list is consistent and it won't be randomized by the ASF app itself.

I wrote this imple tool for myself to simply randomize the list of games to idle while using ASF. 

Need to edit the config.json with the following:
```
  "ASFPath": path to your ASF directory, or you can just simple run the tool inside ASF,
  "refreshTime": time (in seconds) before next refresh,
  "configFile": "config/test.json" - under ASF/config there will be many json, point to the one that will apply,
  "ownedGames": "config/ownedGames.json" - list will be cached here, delete this file to retrieve from Steam Again,
  "steamKey": ".." - Your steam api key, retrieve it here: http://steamcommunity.com/dev/apikey,
  "steamIds": ".." - Your steam ids to get the game list from
```

## Docker commands

```bash
    
        // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath

        
        // run a docker container in daemon mode with ports exposed
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>




```
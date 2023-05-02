# Redis Bot detector
Simple Bot detector/spawner from example provided at https://realpython.com/python-redis/#allowed-key-types

## Usage
Ensure you have a running instance of Redis, for my example I used a docker image containing redis and it must be 
on localhost on port 6379. One the bot_detector has connected to redis, when we run the bot_spawner, it will mimic
the connection of various clients and set a hard limit of no more than 15 connections in a minute, otherwise it will
be deemed a bot.
```
python3 bot_detector.py
python3 bot_spawner.py
```

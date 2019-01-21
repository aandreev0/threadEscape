# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
import yaml
from games.lab_escape.Game import Game
import time

with open("creds.yaml", 'r') as stream:
    try:
        creds = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

ACCESS_TOKEN    = creds['ACCESS_TOKEN']
ACCESS_SECRET   = creds['ACCESS_SECRET']
CONSUMER_KEY    = creds['CONSUMER_KEY']
CONSUMER_SECRET = creds['CONSUMER_SECRET']

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------

print(api.me().id)

currentGames = []

def checkForNewGames():

    for status in tweepy.Cursor(api.mentions_timeline).items(5):
        if status.user.id_str != api.me().id_str: # ignore bot's tweets
            if status.in_reply_to_status_id:
                print("Someone replied -- probably old game with ", status.user.name)
                # here goes code for resuming games
            else:
                print("let's start new game with ", status.user.id_str)
                new_game = Game(status.user.name, status.id_str)
                currentGames.append(new_game)
                postToThread(new_game.parseInput('look'),new_game.clientID)

def postToThread(str, thread):
    split_str = str.split(" ")
    output_buffer = ""
    messages = []
    print("Posting to thread #%s" % thread)
    for idx,elem in enumerate(split_str):
        if len(output_buffer)>=100 or idx == len(split_str)-1: # form a message if buffer filled or no more elements
            output_buffer = output_buffer
            if not idx == len(split_str)-1:
                output_buffer += "..."
            else:
                output_buffer+=" "+elem
            messages.append(output_buffer)
            #print(message_counter, output_buffer)
            output_buffer = ""
        else:
            output_buffer += (" "+elem)
    status = False
    reply_id = thread
    for mid,msg in enumerate(messages):
        #print()
        s = "%s %d/%d" % (msg, mid+1, len(messages))
        if status:
            reply_id = status.id_str
        status = api.update_status(s, in_reply_to_status_id=reply_id, auto_populate_reply_metadata = True)


def processGame(game):
    print(game)



while True:
    print(time.time(), ": " + "Checking the status of games")
    checkForNewGames()
    for game in currentGames:
        processGame(game)
    break
    time.sleep(60) # sleep minute

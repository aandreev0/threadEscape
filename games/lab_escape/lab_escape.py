import yaml
from Door import Door
from Key import Key
from Drawer import Drawer
from Game import Game
inventory = []

# inti DESCRIPTIONS
with open("descriptions.yaml", 'r') as stream:
    try:
        DESCRIPTIONS = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# init objects and game
game = Game("LocalTester")
key = Key(DESCRIPTIONS['door_key'], 1)
door = Door(DESCRIPTIONS['door'], key.id)
drawer = Drawer(DESCRIPTIONS['drawer'])
playing = True

def process(inp):
    global playing
    inp = inp.replace(' the ',' ')
    #print ">>"+inp+"<<"
    if inp == 'look':
        return DESCRIPTIONS['room']
    elif inp == 'look at desk':
        return DESCRIPTIONS['desk']
    elif inp == 'look at door':
        return door.description()

    elif inp=="look at drawer":
        return drawer.description
    elif inp=="inspect drawer":
        return drawer.inspect()
    elif inp=="open drawer":
        return drawer.open()
    elif inp=="close drawer":
        return drawer.close()
    elif inp=="take key from drawer":
        res,str = drawer.take("key")
        if res:
            inventory.append("key")
        return str
    elif inp=="inventory":
        if len(inventory) > 0:
            return "Here is your stuff:\n  "+"\n  ".join(inventory)
        else:
            return "You are carrying nothing of use"
    elif inp=="exit lab":
        if door.closed:
            return "The door is closed!"
        else:
            playing = False
            return "Congratualtions, you escaped the lab!"

    elif inp=="open door":
        return door.open()
    elif inp=="close door":
        return door.close()

    elif inp=="unlock door":
        return door.unlock()
    elif inp=="lock door":
        return door.lock()
    elif inp=="look at key":
        return key.description
    else:
        return "Hmm, I don't know that one"


actions = 0
# Welcome screen
print "=================================================================================="
print "== ESCAPE LAB == ADVENTURE GAME == USE WHATEVER YOU CAN FIND TO GET OUT OF HERE =="
print "=================================================================================="
print DESCRIPTIONS['room']

def act(s):
    global actions
    actions += 1
    print(" %03d:\n%s" % (actions, process(s)))

"""
#   Sample game, uncomment to run
    act("exit the lab")
    act("inventory")
    act("open drawer")
    act("take key from drawer")
    act("inventory")
    act("open door")
    act("unlock door")
    act("open door")
    act("exit the lab")
"""

while playing:
    inp = raw_input(">")
    act(inp)

print " == Game over =="

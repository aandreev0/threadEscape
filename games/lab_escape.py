import yaml
import Door
import Key
inventory = ()

# inti DESCRIPTIONS
with open("descriptions.yaml", 'r') as stream:
    try:
        DESCRIPTIONS = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# init objects
key = Key.Key(DESCRIPTIONS['door_key'], 1)
door = Door.Door(DESCRIPTIONS['door'], key.id)


def process(inp):
    inp = inp.replace(' the ',' ')
    print ">>"+inp+"<<"
    if inp == 'look':
        return DESCRIPTIONS['room']
    elif inp == 'look at desk':
        return DESCRIPTIONS['desk']
    elif inp == 'look at door':
        return door.description()
    elif inp=="unlock door":
        return door.unlock()
    elif inp=="lock door":
        return door.lock()
    elif inp=="look at key":
        return key.description
    else:
        return "Hmm, I don't know that one"


actions = 0
print DESCRIPTIONS['room']
while True:
    inp = raw_input(">")
    actions += 1
    print(" %03d:\n%s" % (actions, process(inp)))

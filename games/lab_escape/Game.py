import yaml
from Door import Door
from Key import Key
from Drawer import Drawer
from Mob import Mob

class Game:
    def __init__(self, playerName):
        # initializing player
        self.player = Mob(playerName)

        # loading descriptions
        with open("descriptions.yaml", 'r') as stream:
            try:
                self.DESCRIPTIONS = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        # loading items
        self.key = Key(self.DESCRIPTIONS['door_key'])
        self.door = Door(self.DESCRIPTIONS['door'], self.key.id)
        self.drawer = Drawer(self.DESCRIPTIONS['drawer'])

        self.playing = True
        self.actions = 0

        print "Started game for "+self.player.name


    def parseInput(self, s):
        self.actions += 1
        print(" %03d:%s\n%s" % (self.actions, s, self.process(s)))


    def process(self, inp):
        inp = inp.replace(' the ',' ')
        #print ">>"+inp+"<<"
        if inp == 'look':
            return self.DESCRIPTIONS['room']
        elif inp == 'look at desk':
            return self.DESCRIPTIONS['desk']
        elif inp == 'look at door':
            return self.door.description()

        elif inp=="look at drawer":
            return self.drawer.description
        elif inp=="inspect drawer":
            return self.drawer.inspect()
        elif inp=="open drawer":
            return self.drawer.open()
        elif inp=="close drawer":
            return self.drawer.close()
        elif inp=="take key from drawer":
            return self.player.take(self.drawer,'key')
        elif inp=="inventory":
            return self.player.ShowInventory()

        elif inp=="exit lab":
            if self.door.closed:
                return "The door is closed!"
            else:
                self.playing = False
                return "Congratualtions, you escaped the lab!"

        elif inp=="open door":
            return self.door.open()
        elif inp=="close door":
            return self.door.close()

        elif inp=="unlock door":
            return self.player.unlock(self.door,self.key)
        elif inp=="lock door":
            return self.door.lock()
        elif inp=="look at key":
            return self.key.description
        else:
            return "Hmm, I don't know that one"

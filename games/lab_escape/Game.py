import yaml
from Door import Door
from Key import Key
from Drawer import Drawer
from Mob import Mob
from Puzzle import Puzzle
import os
class Game:
    def __init__(self, playerName, clientID):
        # initializing player
        self.player = Mob(playerName)
        self.clientID = clientID
        # loading descriptions
        with open(os.path.dirname(__file__)+"/descriptions.yaml" , 'r') as stream:
            try:
                self.DESCRIPTIONS = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        # loading items
        self.key = Key('door key', self.DESCRIPTIONS['door_key'])
        self.door = Door(self.DESCRIPTIONS['door'], self.key)

        self.drawer = Drawer(self.DESCRIPTIONS['drawer'])
        self.drawer.add_item(self.key)

        self.solution = Key('puzzle solution', "This is a solution to a puzzle")
        self.drawer.add_item(self.solution)
        self.puzzle = Puzzle("Some puzzle",self.solution)

        self.playing = True
        self.actions = 0

        print "Started game for "+self.player.name


    def parseInput(self, s):
        self.actions += 1
        return(" %03d>%s\n%s" % (self.actions, s, self.process(s)))


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
            return self.player.take(self.drawer, self.key)
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
            return self.player.unlock(self.door)
        elif inp=="lock door":
            return self.door.lock()
        elif inp=="look at key":
            return self.key.description
        elif inp=="take solution from drawer":
            return self.player.take(self.drawer, self.solution)
        elif inp=="solve puzzle":
            return self.puzzle.solve(self.player)
        else:
            return "Hmm, I don't know that one"

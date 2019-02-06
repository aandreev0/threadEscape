class Game:
    def __init__(self):
        self.playing = True
        self.turns = 1
    def parseInput(self, s):
        self.turns += 1
        if s == "look":
            return "You are in the middle of laboratory. There is a lot of equipment and door leading outside"
        elif s =="exit the lab":
            self.playing = False
            return "Congratulations, you've escaped the lab!"
        else:
            return "Sorry, I don't know what you mean."

game = Game()
while game.playing:
    inp = raw_input("%03d>" % game.turns)
    print ("%s" % game.parseInput(inp))
print "Game over."

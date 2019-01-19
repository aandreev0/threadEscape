from Game import Game

# inti DESCRIPTIONS

# init objects and game



# Welcome screen
print "=================================================================================="
print "== ESCAPE LAB == ADVENTURE GAME == USE WHATEVER YOU CAN FIND TO GET OUT OF HERE =="
print "=================================================================================="

game = Game('Username')

while game.playing:
    inp = raw_input(">")
    game.parseInput(inp)

print " == Game over =="

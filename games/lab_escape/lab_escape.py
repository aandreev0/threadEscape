from Game import Game

# Welcome screen
print "=================================================================================="
print "== ESCAPE LAB == ADVENTURE GAME == USE WHATEVER YOU CAN FIND TO GET OUT OF HERE =="
print "=================================================================================="

game = Game('Username', 0)
print game.parseInput("look")

while game.playing:
    inp = raw_input(">")
    print game.parseInput(inp)

print " == Game over =="

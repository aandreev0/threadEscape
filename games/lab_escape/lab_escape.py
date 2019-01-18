from Game import Game

# inti DESCRIPTIONS

# init objects and game



# Welcome screen
print "=================================================================================="
print "== ESCAPE LAB == ADVENTURE GAME == USE WHATEVER YOU CAN FIND TO GET OUT OF HERE =="
print "=================================================================================="

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
game = Game('Username')

while game.playing:
    inp = raw_input(">")
    game.parseInput(inp)

print " == Game over =="

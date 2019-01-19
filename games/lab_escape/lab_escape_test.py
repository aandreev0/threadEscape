from Game import Game
# Welcome screen
print "=================================================================================="
print "=================== ESCAPE LAB ===================== TEST SUITE =================="
print "=================================================================================="

game = Game('Test User')

game.parseInput("exit the lab")
game.parseInput("inventory")
game.parseInput("open drawer")
game.parseInput("open drawer")
game.parseInput("inspect drawer")


game.parseInput("take key from drawer")
game.parseInput("inventory")
game.parseInput("open door")
game.parseInput("unlock door")
game.parseInput("look at key")

game.parseInput("open door")
game.parseInput("exit the lab")

while game.playing:
    inp = raw_input(">")
    game.parseInput(inp)

print " == Game over =="

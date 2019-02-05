from Game import Game
# Welcome screen
print "=================================================================================="
print "=================== ESCAPE LAB ===================== TEST SUITE =================="
print "=================================================================================="

game = Game('Test User',0)


test_commands = ['open drawer','open drawer','inspect drawer','solve puzzle','take solution from drawer','solve puzzle']

for cmd in test_commands:
    print game.parseInput(cmd)

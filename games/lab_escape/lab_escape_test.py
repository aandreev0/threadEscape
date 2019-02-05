from Game import Game
# Welcome screen
print "=================================================================================="
print "=================== ESCAPE LAB ===================== TEST SUITE =================="
print "=================================================================================="

game = Game('Test User',0)


test_commands = ['look','look at student','open drawer','open drawer','inspect drawer','solve puzzle','take solution from drawer','solve puzzle']
test_commands = ['look at the door','look at the key','look at the drawer']
for cmd in test_commands:
    print game.parseInput(cmd)

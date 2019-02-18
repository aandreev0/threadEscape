from Object import Object

room = Object('Big laboratory room with one door')

desk   = Object('Desk with one drawer')
drawer = Object('Drawer with some stuff inside')
desk.add_item(drawer)


key    = Object('Key to the door')
papers = Object('Bunch of useless papers')
drawer.add_item(key)
drawer.add_item(papers)

player = Object('You, trying to escape this weird place')

room.add_item(desk)
room.add_item(player)

print room.inspect()

def parseInput(s):
    if s == "look":
        room_description = "You are in the middle of laboratory. There is a lot of equipment and door leading outside.\nIn this room:\n"
        room_description += room.inspect()
        return True, room_description
    elif s =="exit the lab":
        if door.is_open():
            return False, "Congratulations, you've escaped the lab!"
        else:
            return True, "Door is closed"
    else:
        return True, "Sorry, I don't know what you mean."

game = True
turns = 0
while game:
    inp = raw_input(">")
    turns += 1
    game,result = parseInput(inp)
    print ("%d$\n%s" % (turns, result))
print "Game over."

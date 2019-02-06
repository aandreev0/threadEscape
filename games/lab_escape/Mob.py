from Object import Object
class Mob(Object):
    def __init__(self, name, desc):
        Object.__init__(self,name,desc)
        self.inventory = []
        self.room = False
        self.blind = False
    def ShowInventory(self):
        if len(self.inventory) > 0:
            return "Here is your stuff:\n  "+"\n  ".join(map(lambda x: x.name, self.inventory))
        else:
            return "You are carrying nothing of use"

    def unlock(self, door):
        return door.unlock(self)


    def take(self, container, what):
        # if enough space:
        # if hands free: etc...
        res, str = container.take(what)
        if res:
            self.add_item(what)
        return str

    def add_item(self,what):
        self.inventory.append(what)
    def remove_item(self,what):
        self.inventory.remove(what)

    def look(self, object):
        return object.appearance(self)

    def goto(self, room):
        if self.room:
            self.room.remove_object(self)
        self.room = room
        room.add_object(self)
        return self.look(self.room)

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
    def lock(self, door):
        return door.lock(self)


    def take(self, container, what):
        # if enough space:
        # if hands free: etc...
        res, str = container.take(what)
        if res:
            self.add_object(what)
        return str
    def put(self,what,where):
        if what in self.inventory:
            self.remove_object(what)
            where.add_object(what)
            if what.__class__.__name__ == 'Room':
                return ("You put %s on the ground" % str(what))
            else:
                return ("You put %s into %s" % (str(what),str(where)))
        else:
            return "You don't have "+str(what)

    def drop(self,what):
        return self.put(what, self.room)

    def add_object(self,what):
        self.inventory.append(what)
    def remove_object(self,what):
        self.inventory.remove(what)

    def look(self, object):
        return object.appearance(self)

    def goto(self, room):
        if self.room:
            self.room.remove_object(self)
        self.room = room
        room.add_object(self)
        return self.look(self.room)
    #def apperance(self,mob):
    def can_see(self,what):
        return True

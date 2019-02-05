from Object import Object
class Door(Object):
    def __init__(self, name, desc, key):
        Object.__init__(self,name,desc)
        self.init_description = desc
        self.locked = True
        self.key = key
        self.closed = True

    def lock(self):
        if self.locked:
            return "Door is already locked"
            return "Door is now unlocked"
        else:
            self.locked = True
    def unlock(self, who):
        if self.key in who.inventory:
            if self.locked:
                self.locked = False
                self.key.use()
                return "Door is now unlocked"
            else:
                return "Door is already unlocked"
        else:
            return "You don't have the right key"

    def open(self):
        if self.locked:
            return "Door is locked"
        else:
            if self.closed:
                self.closed = False
                return "Done"
            else:
                return "It's already open"

    def close(self):
        if not self.closed:
            self.closed = True
            return "Done"
        else:
            return "It's already closed"

    def appearance(self, mob):
        return self.init_description + "\n   Door is "+ ("" if self.locked else "un") +\
               "locked with key " + str(self.key) + " sitting in container " + str(self.key.container)

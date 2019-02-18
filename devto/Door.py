from Object import Object
class Door(Object):
    def __init__(self,description,key):
        Object.__init__(self,description)
        self.key = key
        self.unlocked = False
        self.opened = False

    def open(self):
        if self.unlocked:
            if not self.opened:
                self.opened = True
                return "Door is no open"
            else:
                return "Door is already open"
        else:
            return "Door is locked"

    def unlock(self, who):
        if self.key not in who.contents:
            return False
        else:
            self.unlocked = True
            return True

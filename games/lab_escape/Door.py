class Door:
    def lock(self):
        if self.locked:
            return "Door is already locked"
            return "Door is now unlocked"
        else:
            self.locked = True
    def unlock(self):
        if self.locked:
            self.locked = False
            return "Door is now unlocked"
        else:
            return "Door is already unlocked"

    def description(self):
        return self.init_description + "\n   Door is "+ ("" if self.locked else "un") +"locked with key " + str(self.keyID)

    def __init__(self, desc, keyID):
        self.init_description = desc
        self.locked = True
        self.keyID = keyID

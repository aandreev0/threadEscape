class Mob:
    def __init__(self,name):
        self.name = name
        self.inventory = []

    def ShowInventory(self):
        if len(self.inventory) > 0:
            return "Here is your stuff:\n  "+"\n  ".join(self.inventory)
        else:
            return "You are carrying nothing of use"

    def unlock(self, door, key):
        return door.unlock(key)

    def take(self, object, what):
        res, str = object.take("key")

        if res:
            self.inventory.append("key")
        return str

class Mob:
    def __init__(self,name):
        self.name = name
        self.inventory = []

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

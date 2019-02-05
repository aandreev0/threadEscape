from Object import Object
class Key(Object):
    def __init__(self, name, desc):
        Object.__init__(self,name,desc)
        self.id = id(self)
    def use(self):
        self.description = "This key was used already."

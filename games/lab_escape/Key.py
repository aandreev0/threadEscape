class Key:
    def __init__(self, name, desc):
        self.description = desc
        self.id = id(self)
        self.name = name
    def use(self):
        self.description = "This key was used already."

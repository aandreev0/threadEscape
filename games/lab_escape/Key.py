class Key:
    def __init__(self,desc):
        self.description = desc
        self.id = id(self)
    def use(self):
        self.description = "This key was used already and pretty useless"

class Object:
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        self.mobs = []
        self.container = False
    def appearance(self, mob):
        return self.description

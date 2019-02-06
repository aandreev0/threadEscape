class Object:
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        self.hidden = False
        self.invisible = False
    def appearance(self, observer):
        if observer.blind:
            return False
        else:
            return self.description

class Object:
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        self.hidden = False
        self.invisible = False
    def appearance(self, observer):
        if observer.can_see(self):
            return self.description
        else:
            return "I don't see it here..."
    def presentation(self,observer): # "Small object [lying on the ground]" or "Small object [in your possession]"
        if observer.can_see(self):
            return self.name
        else:
            return "I don't see it here..."

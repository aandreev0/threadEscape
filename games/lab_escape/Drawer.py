from Container import Container
class Drawer(Container):
    def __init__(self,desc):
        Container.__init__(self,desc)
        self.ever_opened = False
        self.contents = ["key"]

    def open(self):
        if self.ever_opened == False: # first-time opening
            if self.closed == True:
                self.closed = False
                self.ever_opened = True
                s = "Large rat jumped out of the drawer at you. You should INSPECT the DRAWER to look inside"
                self.description = "Regular desk drawer"
                return s
        else: # already opened => normal container now
            return Container.open(self)

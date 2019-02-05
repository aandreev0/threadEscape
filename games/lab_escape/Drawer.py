from Container import Container
class Drawer(Container):
    def __init__(self,name, desc):
        Container.__init__(self,name,desc)
        self.ever_opened = False
        self.contents = []
        self.player_warned = False

    def open(self):
        if self.ever_opened == False: # first-time opening
            if self.player_warned == True:
                if self.closed == True:
                    self.closed = False
                    self.ever_opened = True
                    s = "Large rat jumped out of the drawer nearly killing you.\nYou can INSPECT the DRAWER to look inside"
                    self.description = "Regular desk drawer"
                    return s
            else:
                self.player_warned = True
                return "You approached drawer but got scared of weird noises. Sounds like something might rattle inside.\n Maybe you should get something to protect you, or continue to OPEN the DRAWER"
        else: # already opened => normal container now
            return Container.open(self)

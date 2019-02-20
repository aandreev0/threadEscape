from Openable import Openable
from Container import Container
from Object  import Object
class Drawer(Object, Openable, Container):
    def __init__(self,description):
        Object.__init__(self, description)
        Container.__init__(self)
        Openable.__init__(self, key=False)
        self.attemped_to_open = False

    def before_open(self, who):
        if not self.attemped_to_open:
            self.attemped_to_open = True
            return False, "  When you reached to open the drawer you heard weird nosie and got scared. Maybe you should back off?"
        else:
            return True, ''
    def open(self, who):

        s, txt = self.before_open(who)
        if s:
            return Openable.open(self,who)
        else:
            return txt
        return False

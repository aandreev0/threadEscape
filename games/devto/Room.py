from Container import Container
from Object import Object
class Room(Object, Container):
    def __init__(self,description,exits=False):
        Object.__init__(self, description)
        Container.__init__(self)
        self.exits = exits

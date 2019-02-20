from Object import Object
from Container import Container
class Mob(Object, Container):
    def __init__(self, description):
        Object.__init__(self, description)
        Container.__init__(self)

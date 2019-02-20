from Openable import Openable
from Container import Container
from Object  import Object
class Desk(Object, Openable, Container):
    def __init__(self,description):
        Object.__init__(self, description)
        Container.__init__(self)
        Openable.__init__(self, key=False)

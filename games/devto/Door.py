from Openable import Openable
from Object import Object
class Door(Object,Openable):
    def __init__(self,description,key=False):
        Object.__init__(self,description)
        Openable.__init__(self,key)

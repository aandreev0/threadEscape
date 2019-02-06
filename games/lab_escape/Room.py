from Object import Object

class Room(Object):
    def __init__(self, name, desc):
        Object.__init__(self,name,desc)
        self.objects = []

    def add_object(self,object):
        self.objects.append(object)
        return True
    def remove_object(self, object):
        if object in self.objects:
            self.objects.remove(object)
            return True

    def appearance(self,mob):
        s= "  "+self.name+"\n"+self.description
        mobs_str = "\n".join( map(lambda x: x.name+" ["+str(x)+"] is hanging around here", filter(lambda x: not x == mob , self.mobs())))
        if len(mobs_str)>1:
            s += "\n"+mobs_str
        return s

    def mobs(self):
        return filter(lambda x: x.__class__.__name__ == 'Mob' , self.objects)

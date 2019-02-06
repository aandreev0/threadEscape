from Object import Object

class Room(Object):
    def __init__(self, name, desc):
        Object.__init__(self,name,desc)
        self.objects = []
        self.dark = False

    def add_object(self,object):
        self.objects.append(object)
        return True
    def remove_object(self, object):
        if object in self.objects:
            self.objects.remove(object)
            return True

    def appearance(self,mob):
        if not self.dark:
            s= "  "+self.name+"\n"+self.description
            items_str = "\n".join( map(lambda x: x.name+" ["+str(x)+"] is lying on the floor here", self.items()))
            if len(items_str)>1:
                s += "\n"+items_str

            mobs_str = "\n".join( map(lambda x: x.name+" ["+str(x)+"] is hanging around here", filter(lambda x: not x == mob , self.mobs())))
            if len(mobs_str)>1:
                s += "\n"+mobs_str
            return s
        else:
            return "It's dark here..."

    def mobs(self):
        return filter(lambda x: x.__class__.__name__ == 'Mob' , self.objects)
    def items(self):
        return filter(lambda x: not x.__class__.__name__ == 'Mob' , self.objects)

from Object import Object

class Room(Object):
    def __init__(self, name, desc):
        Object.__init__(self,name,desc)

    def add_mob(self,mob):
        self.mobs.append(mob)
        return True
    def remove_mob(self, mob):
        if mob in self.mobs:
            self.mobs.remove(mob)
    def appearance(self,mob):
        print(self.mobs)
        print("List of mobs that are not looking")
        print(filter(lambda x: not x == mob , self.mobs))
        return self.description+"\n" + "\n".join( map(lambda x: x.name+" is hanging around here", filter(lambda x: not x == mob , self.mobs)))

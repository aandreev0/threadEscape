from Object import Object
class Openable(Object):
    def __init__(self,description,key):
      Object.__init__(self,description)
      self.key = key
      self.unlocked = False
      self.opened = False

    def open(self,who):
        if self.unlocked:
            if not self.opened:
                self.opened = True
                return self.short_name + " is now open"
            else:
                return self.short_name + " is already open"
        else:
            return self.short_name + " is locked"

    def unlock(self, who):
        if self.key:
            if self.key in who.contents:
                return 'You unlocked the '+ self.short_name
                self.unlocked = True
            else:
                return 'You do not have the right key'
        else:
            return False

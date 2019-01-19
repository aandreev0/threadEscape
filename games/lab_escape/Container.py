class Container:
    def __init__(self,desc):
        self.description = desc
        self.closed = True
        self.contents = []

    def open(self):
        if self.closed:
            self.closed = False
            return "Done"
        else:
            return "It's already open"

    def close(self):
        if not self.closed:
            self.closed = True
            return "Done"
        else:
            return "It's already closed"

    def inspect(self):
        s = ""
        if self.closed:
            s =  "It is closed"
        else:
            if len(self.contents)>0:
                print self.contents
                s += "There is something in there:\n  " + "\n  ".join(map(lambda x: x.name, self.contents))
            else:
                s+= "Nothing here"
        return s

    def add_item(self,what):
        self.contents.append(what)
    def remove_item(self,what):
        self.contents.remove(what)

    def take(self, what):
        if self.closed:
            return False, "This is closed"
        else:
            if what in self.contents:
                self.remove_item(what)
                return True, "You took "+ what.name + ". Good idea, might come in handy!"
            else:
                return False, "There is no "+what.name+ " here"

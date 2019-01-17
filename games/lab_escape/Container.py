class Container:
    def __init__(self,desc):
        self.description = desc
        self.closed = True
        self.contents = ["Item 1",'Item 2']

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
                s += "There is something in there:\n  " + "\n  ".join(self.contents)
            else:
                s+= "Nothing here"
        return s

    def take(self, what):
        if self.closed:
            return False,"This is closed"
        else:
            if what in self.contents:
                self.contents.remove(what)
                return True, "You took "+ what + ". Good idea, might come in handy!"
            else:
                return False, "There is no "+what+ " here"

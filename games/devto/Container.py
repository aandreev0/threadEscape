class Container():
    def __init__(self):
        self.contents = []

    def add_item(self,item):
        self.contents.append(item)
        return True

    def remove_item(self,item):
        if item in self.contents:
            self.contents.remove(item)
            return True
        else:
            return False

    def inspect(self):
        return "\n".join(map(lambda x: x.short_name + " is in the " + self.short_name, self.contents))

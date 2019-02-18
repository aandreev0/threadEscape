class Object():
    def __init__(self,description):
        self.contents = []
        self.description = description

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
        return "\n".join(map(lambda x: x.description, self.contents))

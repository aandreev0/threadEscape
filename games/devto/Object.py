class Object():
    def __init__(self,description):
        self.contents = []
        if type(description) is str:
            split_desc = description.split(' ')
            description = [split_desc[0], description]

        self.short_name = description[0]
        self.description = description[1]

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

class Object():
    def __init__(self,description):
        if type(description) is str:
            split_desc = description.split(' ')
            description = [split_desc[0], description]

        self.short_name = description[0]
        self.description = description[1]

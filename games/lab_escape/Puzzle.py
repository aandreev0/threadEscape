class Puzzle:
    def __init__(self,name,solution):
        self.name = name
        self.solved = False
        self.solution = solution

    def solve(self, mob):
        if self.solution in mob.inventory:
            self.solved = True
            return "You solved the puzzle!"
        else:
            return "You don't seem to have the required solution to this puzzle"

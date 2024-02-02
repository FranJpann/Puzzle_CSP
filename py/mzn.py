import minizinc


class Solveur:
    def __init__(self, file):
        self.model = minizinc.Model(file)
        self.gecode = minizinc.Solver.lookup("gecode")
        self.problem = minizinc.Instance(self.gecode, self.model)

    def getSolutions(self):
        return self.problem.solve(all_solutions=False)

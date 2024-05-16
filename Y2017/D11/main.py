from utils import Solver, get_data


class Solver2017Day11(Solver):
    YEAR = 2017
    DAY = 11

    def __init__(self, src):
        self.queries = src.strip().split(',')
        self.ans1 = self.ans2 = None

    dirs = {'n': (0, 1), 'ne': (1, 1), 'se': (1, 0), 's': (0, -1), 'sw': (-1, -1), 'nw': (-1, 0)}

    def _dis(self, x, y):
        if x * y >= 0:
            return max(abs(x), abs(y))
        else:
            return abs(x) + abs(y)

    def run(self):
        self.ans2 = 0
        x = y = 0
        for s in self.queries:
            x += self.dirs[s][0]
            y += self.dirs[s][1]
            self.ans2 = max(self.ans2, self._dis(x, y))
        self.ans1 = self._dis(x, y)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2017Day11.YEAR, Solver2017Day11.DAY)
    sol = Solver2017Day11(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

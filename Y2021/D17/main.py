import re
from itertools import count

from utils import Solver, get_data


class Solver2021Day17(Solver):
    YEAR = 2021
    DAY = 17

    def __init__(self, src):
        pat = re.compile(r'(-?\d+)')
        ls = list(map(int, pat.findall(src.strip())))
        self.x, self.y = (ls[0], ls[1]), (ls[2], ls[3])
        self.ans1 = self.ans2 = None

    def _cal(self, dx, dy, t):
        if t <= dx:
            x = (dx + dx - t + 1) * t // 2
        else:
            x = (dx + 1) * dx // 2
        y = dy * t - t * (t - 1) // 2
        return x, y

    def _arrive(self, dx, dy):
        for t in count():
            x, y = self._cal(dx, dy, t)
            if y < self.y[0] or x > self.x[1]:
                return False
            if self.x[0] <= x <= self.x[1] and self.y[0] <= y <= self.y[1]:
                return True

    def run(self):
        self.ans1 = self.ans2 = 0
        for dx in range(1, self.x[1] + 1):
            if dx * (dx + 1) // 2 < self.x[0]:
                continue
            for dy in range(self.y[0], max(abs(self.y[0]), abs(self.y[1])) + 1):
                val = self._cal(dx, dy, dy)[1]
                if self._arrive(dx, dy):
                    self.ans1 = max(self.ans1, val)
                    self.ans2 += 1

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day17.YEAR, Solver2021Day17.DAY)
    # src = 'x=20..30, y=-10..-5'
    sol = Solver2021Day17(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

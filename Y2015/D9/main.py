import re
from itertools import permutations

from utils import Solver, get_data


class Solver2015Day9(Solver):
    YEAR = 2015
    DAY = 9

    def __init__(self, src):
        pat = re.compile(r"(\w+) to (\w+) = (\d+)")
        self.st = set()
        self.mp = {}
        for u, v, w in pat.findall(src.strip()):
            self.mp[u, v] = self.mp[v, u] = int(w)
            self.st |= {u, v}

    def solve_part_1(self):
        return min(sum(self.mp[p[i], p[i + 1]] for i in range(len(self.st) - 1)) for p in permutations(self.st))

    def solve_part_2(self):
        return max(sum(self.mp[p[i], p[i + 1]] for i in range(len(self.st) - 1)) for p in permutations(self.st))


if __name__ == "__main__":
    src = get_data(Solver2015Day9.YEAR, Solver2015Day9.DAY)
    sol = Solver2015Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

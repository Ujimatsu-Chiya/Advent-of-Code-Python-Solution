import re
from itertools import permutations

from utils import Solver, get_data


class Solver2015Day9(Solver):
    YEAR = 2015
    DAY = 9

    def parse(self, src):
        pat = re.compile(r"(\w+) to (\w+) = (\d+)")
        return [(v[0], v[1], int(v[2])) for v in pat.findall(src)]

    def solve_part_1(self, src):
        ls = self.parse(src)
        mp = {}
        st = set()
        for x, y, w in ls:
            mp[x, y] = mp[y, x] = w
            st |= {x, y}
        n = len(st)
        return min(sum(mp[p[i], p[i + 1]] for i in range(n - 1)) for p in permutations(st))

    def solve_part_2(self, src):
        ls = self.parse(src)
        mp = {}
        st = set()
        for x, y, w in ls:
            mp[x, y] = mp[y, x] = w
            st |= {x, y}
        n = len(st)
        return max(sum(mp[p[i], p[i + 1]] for i in range(n - 1)) for p in permutations(st))


if __name__ == "__main__":
    sol = Solver2015Day9()
    src = get_data(Solver2015Day9.YEAR, Solver2015Day9.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

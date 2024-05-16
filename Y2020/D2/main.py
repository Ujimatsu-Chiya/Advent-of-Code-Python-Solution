import re

from utils import Solver, get_data


class Solver2020Day2(Solver):
    YEAR = 2020
    DAY = 2

    def __init__(self, src):
        pat = re.compile(r"(\d+)-(\d+)\s([a-z]):\s([a-z]+)")
        self.queries = [[int(v[0]), int(v[1]), v[2], v[3]] for v in pat.findall(src.strip())]

    def solve_part_1(self):
        return sum(1 for l, r, ch, s in self.queries if l <= s.count(ch) <= r)

    def solve_part_2(self):
        return sum(1 for l, r, ch, s in self.queries if (s[l - 1] == ch) ^ (s[r - 1] == ch))


if __name__ == "__main__":
    src = get_data(Solver2020Day2.YEAR, Solver2020Day2.DAY)
    sol = Solver2020Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

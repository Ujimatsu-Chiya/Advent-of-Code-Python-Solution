import re

from utils import Solver, get_data


class Solver2016Day20(Solver):
    YEAR = 2016
    DAY = 20

    def __init__(self, src):
        pat = re.compile(r"(\d+)-(\d+)")
        self.seg = sorted(list(map(int, tp)) for tp in pat.findall(src.strip()))

    def solve_part_1(self):
        if self.seg[0][0] != 0:
            return 0
        pre = 0
        for x, y in self.seg:
            if x > pre + 1:
                return pre + 1
            pre = y
        return self.seg[-1][1] + 1

    def solve_part_2(self):
        a = []
        ans = 1 << 32
        for l, r in self.seg:
            if len(a) > 0 and l <= a[-1][1] + 1:
                a[-1][1] = max(a[-1][1], r)
            else:
                a.append([l, r])
        for l, r in a:
            ans -= r - l + 1
        return ans


if __name__ == "__main__":
    src = get_data(Solver2016Day20.YEAR, Solver2016Day20.DAY)
    sol = Solver2016Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

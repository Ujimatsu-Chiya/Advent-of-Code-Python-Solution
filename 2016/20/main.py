import re

from utils import Solver, get_data


class Solver2016Day20(Solver):
    YEAR = 2016
    DAY = 20

    def parse(self, src):
        pat = re.compile(r"(\d+)-(\d+)")
        ls = []
        for tp in pat.findall(src.strip()):
            ls.append(list(map(int, tp)))
        return ls

    def solve_part_1(self, src):
        ls = sorted(self.parse(src))
        if ls[0][0] != 0:
            return 0
        pre = 0
        for x, y in ls:
            if x > pre + 1:
                return pre + 1
            pre = y
        return ls[-1][1] + 1

    def solve_part_2(self, src):
        ls = sorted(self.parse(src))
        a = []
        ans = 1 << 32
        for l, r in ls:
            if len(a) > 0 and l <= a[-1][1] + 1:
                a[-1][1] = max(a[-1][1], r)
            else:
                a.append([l, r])
        for l, r in a:
            ans -= r - l + 1
        return ans


if __name__ == "__main__":
    sol = Solver2016Day20()
    src = get_data(Solver2016Day20.YEAR, Solver2016Day20.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

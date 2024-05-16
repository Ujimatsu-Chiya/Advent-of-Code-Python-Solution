import re
from collections import Counter
from itertools import count

from utils import Solver, get_data


class Solver2017Day20(Solver):
    YEAR = 2017
    DAY = 20

    def __init__(self, src):
        pat = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>,\s*v=<(-?\d+),(-?\d+),(-?\d+)>,\s*a=<(-?\d+),(-?\d+),(-?\d+)>")
        self.ls = []
        for tp in pat.findall(src.strip()):
            p = tuple(map(int, tp[0:3]))
            v = tuple(map(int, tp[3:6]))
            a = tuple(map(int, tp[6:9]))
            self.ls.append((p, v, a))

    def _cal_pos(self, pt, tm):
        return tuple((p + v * tm + a * (tm + 1) * tm // 2) for p, v, a in zip(*pt))

    def solve_part_1(self):
        def dis(pt, tm):
            return sum(abs(p) for p in self._cal_pos(pt, tm))

        t = 1
        cnt = 0
        pre = []
        while True:
            a = sorted([[dis(self.ls[i], t), i] for i in range(len(self.ls))])
            b = [v[1] for v in a]
            if b == pre:
                cnt += 1
                if cnt == 5:
                    break
            else:
                cnt = 0
                pre = b

            t *= 10
        return pre[0]

    def solve_part_2(self):
        ls = sorted(self.ls)
        pre = len(ls)
        cnt = 0
        for tm in count():
            lt = [self._cal_pos(pt, tm) for pt in ls]
            c = Counter(lt)
            ls = [ls[i] for i in range(len(ls)) if c[lt[i]] == 1]
            if len(ls) == pre:
                cnt += 1
                if cnt == 200:
                    break
            else:
                pre = len(ls)
                cnt = 0
        return len(ls)


if __name__ == "__main__":
    src = get_data(Solver2017Day20.YEAR, Solver2017Day20.DAY)
    sol = Solver2017Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from itertools import product, permutations, combinations
from collections import defaultdict

from utils import Solver, get_data


class Solver2021Day19(Solver):
    YEAR = 2021
    DAY = 19

    def __init__(self, src):
        self.scanners = [[tuple(map(int, t.split(','))) for t in s.split('\n')[1:]] for s in src.strip().split('\n\n')]
        self.ans1 = self.ans2 = None

    def trans(self, pos, t):
        per = t[3]
        return tuple(pos[per[i]] * t[i] for i in range(3))

    def reshape(self, standard, calibration):
        for ori in product([-1, 1], [-1, 1], [-1, 1], permutations(range(3))):
            mp = defaultdict(int)
            now = [self.trans(vec, ori) for vec in calibration]
            for u in standard:
                for v in now:
                    mp[v[0] - u[0], v[1] - u[1], v[2] - u[2]] += 1
            if max(mp.values()) >= 12:
                d = next(key for key, val in mp.items() if val >= 12)
                return [tuple(v[i] - d[i] for i in range(3)) for v in now], d

    def run(self):
        m = len(self.scanners)
        vis = {0}
        st = set(self.scanners[0])
        pos = [[] for _ in range(m)]
        pos[0] = [0, 0, 0]
        match = [[] for _ in range(m)]
        match[0] = self.scanners[0]
        pre = [0]
        while len(pre) > 0:
            now = []
            for i in pre:
                for j in range(m):
                    if j in vis:
                        continue
                    res = self.reshape(match[i], self.scanners[j])
                    if res is None:
                        continue
                    match[j], pos[j] = res
                    now.append(j)
                    vis.add(j)
                    st |= set(match[j])
            pre = now
        self.ans1 = len(st)
        self.ans2 = max(sum(abs(x - y) for x, y in zip(u, v)) for u, v in combinations(pos, 2))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day19.YEAR, Solver2021Day19.DAY)
    sol = Solver2021Day19(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

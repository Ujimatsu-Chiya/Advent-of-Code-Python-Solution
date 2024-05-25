from collections import defaultdict

from utils import Solver, get_data


class Solver2021Day20(Solver):
    YEAR = 2021
    DAY = 20

    def __init__(self, src):
        s1, s2 = src.strip().split('\n\n')
        self.rules = [int(ch == '#') for ch in s1.strip()]
        self.mp = [[int(ch == '#') for ch in u] for u in s2.split()]

    def _run(self, T):
        n, m = len(self.mp), len(self.mp[0])
        mp = defaultdict(int)
        for i in range(n):
            for j in range(m):
                mp[i, j] = self.mp[i][j]
        dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        msk = (1 << len(dirs)) - 1
        for t in range(T):
            default = self.rules[mp.default_factory() * msk]
            mq = defaultdict(lambda default=default: default)
            mnx, mxx = -t - 1, n + t
            mny, mxy = -t - 1, m + t
            for i in range(mnx, mxx + 1):
                for j in range(mny, mxy + 1):
                    w = 0
                    for k, d in enumerate(dirs):
                        w |= mp[i + d[0], j + d[1]] << k
                    mq[i, j] = self.rules[w]
            mp = mq
        return sum(mp.values())

    def solve_part_1(self):
        return self._run(2)

    def solve_part_2(self):
        return self._run(50)


if __name__ == "__main__":
    src = get_data(Solver2021Day20.YEAR, Solver2021Day20.DAY)
    sol = Solver2021Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from collections import defaultdict
from itertools import product

from utils import Solver, get_data


class Solver2020Day17(Solver):
    YEAR = 2020
    DAY = 17

    def __init__(self, src):
        self.mp = src.strip().split()

    def solve_part_1(self):
        dirs = [d for d in product(range(-1, 2), repeat=3) if any(v != 0 for v in d)]
        mp = defaultdict(int)
        mxx, mxy = len(self.mp), len(self.mp[0])
        for i in range(mxx):
            for j in range(mxy):
                mp[i, j, 0] = int(self.mp[i][j] == '#')

        M = 6
        for k in range(1, M + 1):
            mq = defaultdict(int)
            for x in range(-k, mxx + k):
                for y in range(-k, mxy + k):
                    for z in range(k + 1):
                        v = sum(mp[x + dx, y + dy, abs(z + dz)] for dx, dy, dz in dirs)
                        mq[x, y, z] = 1 if v == 3 or v == 2 and mp[x, y, z] == 1 else 0
            mp = mq
        return sum(v * (1 + int(k[2] != 0)) for k, v in mp.items())

    def solve_part_2(self):
        dirs = [d for d in product(range(-1, 2), repeat=4) if any(v != 0 for v in d)]
        mp = defaultdict(int)
        mxx, mxy = len(self.mp), len(self.mp[0])
        for i in range(mxx):
            for j in range(mxy):
                mp[i, j, 0, 0] = int(self.mp[i][j] == '#')
        M = 6
        for k in range(1, M + 1):
            mq = defaultdict(int)
            for x in range(-k, mxx + k):
                for y in range(-k, mxy + k):
                    for z in range(k + 1):
                        for w in range(k + 1):
                            v = sum(mp[x + dx, y + dy, abs(z + dz), abs(w + dw)] for dx, dy, dz, dw in dirs)
                            mq[x, y, z, w] = 1 if v == 3 or v == 2 and mp[x, y, z, w] == 1 else 0
            mp = mq
        return sum(v * (1 + int(k[2] != 0)) * (1 + int(k[3] != 0)) for k, v in mp.items())


if __name__ == "__main__":
    src = get_data(Solver2020Day17.YEAR, Solver2020Day17.DAY)
    #     src = '''.#.
    # ..#
    # ###'''
    sol = Solver2020Day17(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

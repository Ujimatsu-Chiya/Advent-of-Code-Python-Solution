from collections import deque, Counter

from utils import Solver, get_data
from itertools import count

class Solver2022Day23(Solver):
    YEAR = 2022
    DAY = 23

    def __init__(self, src):
        ls = src.strip().split()
        self.st = {(i, j) for i in range(len(ls)) for j in range(len(ls[0])) if ls[i][j] == '#'}

    def _run(self, st):
        dir_list = [[[-1, -1], [-1, 0], [-1, 1]],
                    [[1, -1], [1, 0], [1, 1]],
                    [[-1, -1], [0, -1], [1, -1]],
                    [[-1, 1], [0, 1], [1, 1]]]
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        q = deque(range(4))
        while True:
            mp = dict()
            for x, y in st:
                if all((x + dx, y + dy) not in st for dx, dy in dirs):
                    mp[x, y] = x, y
                    continue
                idx = -1
                for i in q:
                    if all((x + dx, y + dy) not in st for dx, dy in dir_list[i]):
                        idx = i
                        break
                if idx >= 0:
                    mp[x, y] = x + dir_list[idx][1][0], y + dir_list[idx][1][1]
                else:
                    mp[x, y] = x, y
            c = Counter(mp.values())
            st = {k if c[v] == 2 else v for k, v in mp.items()}
            yield st
            q.rotate(-1)

    def solve_part_1(self):
        T = 10
        gen = self._run(self.st)
        for _ in range(T):
            st = next(gen)
        mnx, mxx = min(v[0] for v in st), max(v[0] for v in st)
        mny, mxy = min(v[1] for v in st), max(v[1] for v in st)
        return (mxx - mnx + 1) * (mxy - mny + 1) - len(st)

    def solve_part_2(self):
        pre = self.st
        gen = self._run(pre)
        for i in count(1):
            st = next(gen)
            if st == pre:
                return i
            pre = st


if __name__ == "__main__":
    src = get_data(Solver2022Day23.YEAR, Solver2022Day23.DAY)
    sol = Solver2022Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

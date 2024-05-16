from collections import Counter
from itertools import count

from utils import Solver, get_data


class Solver2018Day18(Solver):
    YEAR = 2018
    DAY = 18

    def __init__(self, src):
        s = src.strip().split()
        t = {'.': 0, '|': 1, '#': 2}
        self.mp = tuple(tuple(t[s[i][j]] for j in range(len(s[0]))) for i in range(len(s)))
        self.ans1 = self.ans2 = None

    def run(self):
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        mp = self.mp
        n, m = len(mp), len(mp[0])
        mq = {}
        state_ls = []
        st = T = -1
        for i in count():
            if mp in mq.keys():
                T = i - mq[mp]
                st = mq[mp]
                break
            mq[mp] = i
            state_ls.append(mp)
            ls = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    c = Counter(mp[i + dx][j + dy] for dx, dy in dirs if 0 <= i + dx < n and 0 <= j + dy < m)
                    if mp[i][j] == 0:
                        ls[i][j] = (1 if c.get(1, 0) >= 3 else 0)
                    elif mp[i][j] == 1:
                        ls[i][j] = (2 if c.get(2, 0) >= 3 else 1)
                    else:
                        ls[i][j] = (2 if c.get(2, 0) >= 1 and c.get(1, 0) >= 1 else 0)
            mp = tuple(tuple(v) for v in ls)

        M1 = 10
        M2 = 1000000000
        if st >= M1:
            idx = M1
        else:
            idx = st + (M1 - st) % T
        mp = state_ls[idx]
        self.ans1 = sum(v.count(1) for v in mp) * sum(v.count(2) for v in mp)
        if st >= M2:
            idx = M2
        else:
            idx = st + (M2 - st) % T
        mp = state_ls[idx]
        self.ans2 = sum(v.count(1) for v in mp) * sum(v.count(2) for v in mp)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day18.YEAR, Solver2018Day18.DAY)
    sol = Solver2018Day18(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

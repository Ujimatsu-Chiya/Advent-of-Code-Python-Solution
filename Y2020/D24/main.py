from utils import Solver, get_data
from collections import Counter, defaultdict


class Solver2020Day24(Solver):
    YEAR = 2020
    DAY = 24

    def __init__(self, src):
        self.queries = []
        for s in src.strip().split():
            i = 0
            ops = []
            while i < len(s):
                if s[i] in "we":
                    ops.append(s[i])
                    i += 1
                else:
                    ops.append(s[i:i + 2])
                    i += 2
            self.queries.append(ops)
        self.ans1 = self.ans2 = None

    def run(self):
        dirs_mp = {'ne': (0, 1), 'e': (1, 1), 'se': (1, 0), 'sw': (0, -1), 'w': (-1, -1), 'nw': (-1, 0)}
        trans = [[0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0]]
        a = []
        for ops in self.queries:
            x = y = 0
            for s in ops:
                x += dirs_mp[s][0]
                y += dirs_mp[s][1]
            a.append((x, y))
        now = {p: x & 1 for p, x in Counter(a).items()}
        self.ans1 = sum(now.values())
        M = 100
        dirs = tuple(dirs_mp.values())
        mp = defaultdict(int)
        mp.update(now)
        for i in range(M):
            next_tp = {(x + dx, y + dy) for x, y in mp.keys() for dx, dy in dirs}
            mq = defaultdict(int)
            for sx, sy in next_tp:
                cnt = 0
                for dx, dy in dirs:
                    cnt += mp[sx + dx, sy + dy] == 1
                mq[sx, sy] = trans[mp[sx, sy]][cnt]
            mp = mq
        self.ans2 = sum(mp.values())

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2020Day24.YEAR, Solver2020Day24.DAY)
    sol = Solver2020Day24(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

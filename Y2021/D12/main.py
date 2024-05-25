from utils import Solver, get_data
from collections import defaultdict


class Solver2021Day12(Solver):
    YEAR = 2021
    DAY = 12

    def __init__(self, src):
        self.g = defaultdict(list)
        mp = {}
        pos, neg = 0, -1

        def get_id(s):
            nonlocal pos, neg
            if s in mp.keys():
                return mp[s]
            if s.islower():
                mp[s] = pos
                pos += 1
            else:
                mp[s] = neg
                neg -= 1
            return mp[s]

        for s in src.strip().split():
            l, r = s.split('-')
            self.g[get_id(l)].append(get_id(r))
            self.g[get_id(r)].append(get_id(l))
        self.start, self.end = get_id('start'), get_id('end')

    def solve_part_1(self):
        f = defaultdict(int)
        f[1 << self.start, self.start] = 1
        ids = sorted(self.g.keys(), reverse=True)
        M = max(ids) + 1
        for st in range(1 << M):
            for u in ids:
                if f[st, u] == 0:
                    continue
                for v in self.g[u]:
                    if v < 0:
                        f[st, v] += f[st, u]
                    elif (st >> v & 1) == 0:
                        f[st | 1 << v, v] += f[st, u]
        return sum(f[tp] for tp in f.keys() if tp[1] == self.end)

    def solve_part_2(self):
        ids = sorted(self.g.keys(), reverse=True)
        M = max(ids) + 1
        pw = [1]
        base = 3
        for _ in range(M):
            pw.append(pw[-1] * base)
        f = defaultdict(int)
        f[(base - 1) * base ** self.start, self.start] = 1
        for st in range(base ** M):
            mx = max([st // pw[i] % base for i in range(M) if i != self.start])
            for u in ids:
                if f[st, u] == 0 or u == self.end:
                    continue
                st_ls = [st // pw[i] % base for i in range(M)]
                for v in self.g[u]:
                    if v < 0:
                        f[st, v] += f[st, u]
                    elif st // pw[v] % base == 0 or mx <= 1 and st // pw[v] % base < base - 1:
                        f[st + pw[v], v] += f[st, u]

        return sum(f[tp] for tp in f.keys() if tp[1] == self.end)


if __name__ == "__main__":
    src = get_data(Solver2021Day12.YEAR, Solver2021Day12.DAY)
    sol = Solver2021Day12(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

import re
import numpy as np
from utils import Solver, get_data
from collections import defaultdict
from math import prod


class Solver2020Day20(Solver):
    YEAR = 2020
    DAY = 20

    def __init__(self, src):
        ls = src.strip().split('\n\n')
        self.mp = {}
        pat = re.compile(r"(\d+)")
        for mp_str in ls:
            mp = mp_str.split('\n')
            x = int(pat.findall(mp[0])[0])
            self.mp[x] = np.array([[int(ch == '#') for ch in s] for s in mp[1:]])
        self.ans1 = self.ans2 = None

    def form(self, a):
        for _ in range(2):
            for _ in range(4):
                yield a
                a = np.rot90(a)
            a = np.flip(a, 0)

    def run(self):
        edges = defaultdict(set)
        for k, v in self.mp.items():
            for edge in [v[0], v[-1], v[:, 0], v[:, -1]]:
                edges[k] |= {tuple(edge), tuple(edge[::-1])}
        neigh = {k1: [k2 for k2, v2 in edges.items() if k1 != k2 and v1 & v2] for k1, v1 in edges.items()}
        corners = [k for k, v in neigh.items() if len(v) == 2]
        self.ans1 = prod(corners)
        S = round(len(self.mp) ** 0.5)
        K = len(self.mp[corners[0]])
        mat = np.zeros(((K - 2) * S, (K - 2) * S), dtype=np.int64)
        mp = [[None for _ in range(S)] for _ in range(S)]
        for a in self.form(self.mp[corners[0]]):
            if all(any(e in v and k != corners[0] for k, v in edges.items()) for e in [tuple(a[-1]), tuple(a[:, -1])]):
                mp[0][0] = a
        edges.pop(corners[0])
        for i in range(S):
            for j in range(S):
                if not i == j == 0:
                    v1 = None if i == 0 else tuple(mp[i - 1][j][-1])
                    v2 = None if j == 0 else tuple(mp[i][j - 1][:, -1])
                    st = {v for v in {v1, v2} if v is not None}
                    for k, v in edges.items():
                        if st & v == st:
                            id = k
                    edges.pop(id)
                    for a in self.form(self.mp[id]):
                        if (v1 is None or tuple(a[0]) == v1) and (v2 is None or tuple(a[:, 0]) == v2):
                            mp[i][j] = a
                            break
                mat[i * (K - 2):(i + 1) * (K - 2), j * (K - 2):(j + 1) * (K - 2)] = mp[i][j][1:-1, 1:-1]
        monster_str = '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '
        monster_ls = monster_str.split('\n')
        monster = np.array([[int(ch == '#') for ch in s] for s in monster_ls])
        for a in self.form(mat):
            cnt = 0
            for i in range(len(a) - len(monster) + 1):
                for j in range(len(a[0]) - len(monster[0]) + 1):
                    if (a[i:i + len(monster), j:j + len(monster[0])] + monster == 2).sum() == monster.sum():
                        cnt += 1
            if cnt > 0:
                self.ans2 = a.sum() - cnt * monster.sum()

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2020Day20.YEAR, Solver2020Day20.DAY)
    sol = Solver2020Day20(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

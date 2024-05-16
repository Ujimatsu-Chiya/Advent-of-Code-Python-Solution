from collections import defaultdict

from utils import Solver, get_data


class Solver2019Day24(Solver):
    YEAR = 2019
    DAY = 24

    def __init__(self, src):
        self.mp = tuple({'#': 1, '.': 0}[ch] for ch in src if ch in '#.')

    tran = [[0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]]

    def solve_part_1(self):
        M = 5
        g = [[i for i in range(M * M) if abs(i // 5 - j // 5) + abs(i % 5 - j % 5) == 1] for j in range(M * M)]
        a = self.mp
        st = set()
        while True:
            if a in st:
                return sum(a[i] << i for i in range(M * M))
            st.add(a)
            a = tuple(self.tran[a[i]][sum(a[x] for x in g[i])] for i in range(M * M))

    def solve_part_2(self):
        M = 5
        g = [[(i, 0) for i in range(M * M) if abs(i // 5 - j // 5) + abs(i % 5 - j % 5) == 1 and i != 12] for j in
             range(M * M)]
        g[12] = []
        for i in range(M):
            for j in range(M):
                k = i * M + j
                if i == 0:
                    g[k].append((7, -1))
                    g[7].append((k, 1))
                if j == 0:
                    g[k].append((11, -1))
                    g[11].append((k, 1))
                if i == M - 1:
                    g[k].append((17, -1))
                    g[17].append((k, 1))
                if j == M - 1:
                    g[k].append((13, -1))
                    g[13].append((k, 1))
        f = defaultdict(int)
        for i in range(M * M):
            f[0, i] = self.mp[i]
        T = 200
        for t in range(1, T + 1):
            h = defaultdict(int)
            m = (t + 1) // 2
            for l in range(-m, m + 1):
                for i in range(M * M):
                    h[l, i] = self.tran[f[l, i]][sum(f[l + d, j] for j, d in g[i])]
            f = h
            ls = []
            for l in range(-m, m + 1):
                u = tuple(f[l, i] for i in range(M * M))
                if sum(u) != 0:
                    ls.append(l)
        return sum(f.values())


if __name__ == "__main__":
    src = get_data(Solver2019Day24.YEAR, Solver2019Day24.DAY)
    sol = Solver2019Day24(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

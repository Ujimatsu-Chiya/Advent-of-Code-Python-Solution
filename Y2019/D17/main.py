from itertools import combinations

from tools import IntCodeComputer
from utils import Solver, get_data


class Solver2019Day17(Solver):
    YEAR = 2019
    DAY = 17

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))
        p = IntCodeComputer(self.ops)
        a = p.get_all_output()
        s = "".join(chr(ch) for ch in a)
        self.mp = s.split()

    def solve_part_1(self):
        n, m = len(self.mp), len(self.mp[0])
        ans = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if all(self.mp[x][y] == '#' for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1), (i, j)]):
                    ans += i * j
        return ans

    def solve_part_2(self):
        n, m = len(self.mp), len(self.mp[0])
        L = 20

        def ok(x, y):
            return 0 <= x < n and 0 <= y < m and self.mp[x][y] == '#'

        def gen_path():
            ls = []
            x, y = [[i, j] for i in range(n) for j in range(m) if self.mp[i][j] not in ".#"][0]
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            p = "^>v<".index(self.mp[x][y])
            while True:
                if ok(x + dirs[(p - 1) % 4][0], y + dirs[(p - 1) % 4][1]):
                    ls.append(['L', 0])
                    p = (p - 1) % 4
                elif ok(x + dirs[(p + 1) % 4][0], y + dirs[(p + 1) % 4][1]):
                    ls.append(['R', 0])
                    p = (p + 1) % 4
                else:
                    break
                while ok(x + dirs[p][0], y + dirs[p][1]):
                    x += dirs[p][0]
                    y += dirs[p][1]
                    ls[-1][1] += 1
            return ["{},{}".format(u[0], u[1]) for u in ls]

        def gen_func(ls):
            s_len = [0]
            m = len(ls)
            st = set()
            for s in ls:
                s_len.append(s_len[-1] + len(s))
            for r in range(1, m + 1):
                for l in range(r):
                    if s_len[r] - s_len[l] + r - l - 1 <= L:
                        st.add(tuple(ls[l:r]))
            for comb in combinations(st, 3):
                f = [L for _ in range(m + 1)]
                pre = [-1 for _ in range(m + 1)]
                f[0] = 0
                for j in range(1, m + 1):
                    for k, p in enumerate(comb):
                        if j >= len(p) and ls[j - len(p):j] == p and f[j - len(p)] + 1 < f[j]:
                            f[j] = f[j - len(p)] + 1
                            pre[j] = k

                if f[-1] * 2 - 1 <= L:
                    func = []
                    p = m
                    while p != 0:
                        func.append(chr(ord('A') + pre[p]))
                        p -= len(comb[pre[p]])
                    return ",".join(func[::-1]), *[",".join(v) for v in comb]

        ls = gen_path()
        func_str = gen_func(tuple(ls))
        p = IntCodeComputer(self.ops)
        p.add_ascii_input("\n".join(func_str) + "\nn\n")
        p.ops[0] = 2
        return p.get_all_output()[-1]


if __name__ == "__main__":
    src = get_data(Solver2019Day17.YEAR, Solver2019Day17.DAY)
    sol = Solver2019Day17(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

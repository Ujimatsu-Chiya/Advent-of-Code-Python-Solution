from collections import defaultdict, deque

from utils import Solver, get_data


class Solver2019Day20(Solver):
    YEAR = 2019
    DAY = 20

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def is_space(self, x, y):
        return 0 <= x < len(self.mp) and 0 <= y < len(self.mp[0]) and self.mp[x][y] == '.'

    def __init__(self, src):
        self.mp = src.strip('\n').split('\n')
        n, m = len(self.mp), len(self.mp[0])
        self.pt_list = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if self.mp[i][j].isupper():
                    if j + 1 < m and self.mp[i][j + 1].isupper():
                        tag = self.mp[i][j] + self.mp[i][j + 1]
                        if self.is_space(i, j - 1):
                            self.pt_list[tag].append((i, j - 1))
                        if self.is_space(i, j + 2):
                            self.pt_list[tag].append((i, j + 2))
                    if i + 1 < n and self.mp[i + 1][j].isupper():
                        tag = self.mp[i][j] + self.mp[i + 1][j]
                        if self.is_space(i - 1, j):
                            self.pt_list[tag].append((i - 1, j))
                        if self.is_space(i + 2, j):
                            self.pt_list[tag].append((i + 2, j))
        self.more = defaultdict(list)
        for v in self.pt_list.values():
            for i in range(len(v)):
                for j in range(i):
                    self.more[v[i]].append(v[j])
                    self.more[v[j]].append(v[i])
        v = self.more.keys()
        mnx, mxx = min(u[0] for u in v), max(u[0] for u in v)
        mny, mxy = min(u[1] for u in v), max(u[1] for u in v)
        self.border = {}
        for u in v:
            self.border[u] = -1 if u[0] in [mnx, mxx] or u[1] in [mny, mxy] else 1

    def solve_part_1(self):
        st, ed = self.pt_list["AA"][0], self.pt_list["ZZ"][0]
        d = {}
        q = deque([st])
        d[st] = 0
        while len(q) > 0:
            sx, sy = q.popleft()
            for dx, dy in self.dirs:
                x, y = sx + dx, sy + dy
                if self.is_space(x, y) and (x, y) not in d.keys():
                    d[x, y] = d[sx, sy] + 1
                    q.append((x, y))
            if (sx, sy) in self.more.keys():
                for x, y in self.more[sx, sy]:
                    if (x, y) not in d.keys():
                        d[x, y] = d[sx, sy] + 1
                        q.append((x, y))
        return d[ed]

    def solve_part_2(self):
        st, ed = (*self.pt_list["AA"][0], 0), (*self.pt_list["ZZ"][0], 0)
        d = {}
        q = deque([st])
        d[st] = 0
        while len(q) > 0:
            sx, sy, level = q.popleft()
            if (sx, sy, level) == ed:
                break
            for dx, dy in self.dirs:
                x, y = sx + dx, sy + dy
                if self.is_space(x, y) and (x, y, level) not in d.keys():
                    d[x, y, level] = d[sx, sy, level] + 1
                    q.append((x, y, level))
            if (sx, sy) in self.more.keys():
                delta = self.border[sx, sy]
                for x, y in self.more[sx, sy]:
                    if level + delta >= 0 and (x, y, level + delta) not in d.keys():
                        d[x, y, level + delta] = d[sx, sy, level] + 1
                        q.append((x, y, level + delta))
        return d[ed]


if __name__ == "__main__":
    src = get_data(Solver2019Day20.YEAR, Solver2019Day20.DAY)
    sol = Solver2019Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

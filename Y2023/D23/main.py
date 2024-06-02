from collections import deque, defaultdict

from utils import Solver, get_data


class Solver2023Day23(Solver):
    YEAR = 2023
    DAY = 23

    def __init__(self, src):
        self.mp = src.strip().split()
        self.mp[0] = self.mp[0].replace('.', 'v')
        self.mp[-1] = self.mp[-1].replace('.', 'v')

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def solve_part_1(self):

        mp_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
        n, m = len(self.mp), len(self.mp[0])

        g = {}

        def bfs(ax, ay):
            g[ax, ay] = []
            d = [[-1 for _ in range(m)] for _ in range(n)]
            x, y = ax + self.dirs[mp_dir[self.mp[ax][ay]]][0], ay + self.dirs[mp_dir[self.mp[ax][ay]]][1]
            if not (0 <= x < n and 0 <= y < m):
                return
            d[x][y] = 1
            q = deque([[x, y]])
            while len(q) > 0:
                sx, sy = q.popleft()
                for p, (dx, dy) in enumerate(self.dirs):
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m:
                        if d[x][y] == -1 and self.mp[x][y] == '.':
                            d[x][y] = d[sx][sy] + 1
                            q.append([x, y])
                        elif self.mp[x][y] in mp_dir.keys() and p != mp_dir[self.mp[x][y]] ^ 2:
                            g[ax, ay].append(((x, y), d[sx][sy] + 1))

        for i in range(n):
            for j in range(m):
                if self.mp[i][j] in mp_dir.keys():
                    bfs(i, j)

        st = 0, self.mp[0].find('v')
        ed = n - 1, self.mp[-1].find('v')
        deg = defaultdict(int)
        f = defaultdict(int)
        for vec in g.values():
            for v, _ in vec:
                deg[v] += 1
        cnt = 0
        q = deque()
        for k in g.keys():
            if deg[k] == 0:
                q.append(k)
                f[k] = 0
        while len(q) > 0:
            k = q.popleft()
            cnt += 1
            for v, w in g[k]:
                deg[v] -= 1
                f[v] = max(f[v], f[k] + w)
                if deg[v] == 0:
                    q.append(v)
        return f[ed]

    def solve_part_2(self):
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        n, m = len(self.mp), len(self.mp[0])
        st = 0, self.mp[0].find('v')
        ed = n - 1, self.mp[-1].find('v')
        g = defaultdict(list)
        id_mp = {}

        def get_id(tp):
            if tp not in id_mp.keys():
                id_mp[tp] = len(id_mp)
            return id_mp[tp]

        def is_key(i, j):
            return (i, j) in [st, ed] or self.mp[i][j] != '#' and sum(
                self.mp[i + dx][j + dy] != '#' for dx, dy in dirs) > 2

        def bfs(ax, ay):
            d = [[-1 for _ in range(m)] for _ in range(n)]
            g[get_id((ax, ay))] = []
            d[ax][ay] = 0
            q = deque([[ax, ay]])
            while len(q) > 0:
                sx, sy = q.popleft()
                for p, (dx, dy) in enumerate(self.dirs):
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m:
                        if d[x][y] == -1:
                            if is_key(x, y):
                                g[get_id((ax, ay))].append((get_id((x, y)), d[sx][sy] + 1))
                            elif self.mp[x][y] != '#':
                                d[x][y] = d[sx][sy] + 1
                                q.append([x, y])

        for i in range(n):
            for j in range(m):
                if is_key(i, j):
                    bfs(i, j)
        st, ed = get_id(st), get_id(ed)
        f = {(1 << st, st): 0}
        ans = 0
        while len(f) > 0:
            h = {}
            for (st, u), val in f.items():
                if u == ed:
                    ans = max(ans, val)
                else:
                    for v, w in g[u]:
                        if (st >> v & 1) == 0:
                            nst = st | 1 << v
                            h[nst, v] = max(h.get((nst, v), 0), val + w)
            f = h
        return ans


if __name__ == "__main__":
    src = get_data(Solver2023Day23.YEAR, Solver2023Day23.DAY)
    sol = Solver2023Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
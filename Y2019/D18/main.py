from collections import deque

from utils import Solver, get_data


class Solver2019Day18(Solver):
    YEAR = 2019
    DAY = 18
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, src):
        self.mp = src.strip().split()

    def gen_info(self, mp, sx, sy):
        n, m = len(mp), len(mp[0])
        d = [[-1 for _ in range(m)] for _ in range(n)]
        d[sx][sy] = 0
        q = deque([(sx, sy, '')])
        info = {}
        while len(q) > 0:
            sx, sy, path = q.popleft()
            if mp[sx][sy].isalpha() and d[sx][sy] > 0:
                info[mp[sx][sy]] = (d[sx][sy], path)
                path += mp[sx][sy]
            for dx, dy in self.dirs:
                x, y = sx + dx, sy + dy
                if mp[x][y] != '#' and d[x][y] == -1:
                    d[x][y] = d[sx][sy] + 1
                    q.append((x, y, path))
        return info

    def _run(self, mp):
        path_info = {}
        n, m = len(mp), len(mp[0])
        for i in range(n):
            for j in range(m):
                if mp[i][j].islower() or mp[i][j].isdigit():
                    path_info[mp[i][j]] = self.gen_info(mp, i, j)
        keys = [ch for ch in path_info.keys() if ch.islower()]
        start = tuple(sorted(ch for ch in path_info.keys() if ch.isdigit()) + [0])
        f_mp = {start: 0}
        for _ in range(len(keys)):
            g_mp = {}
            for tp, dis in f_mp.items():
                pos, st = list(tp[:-1]), tp[-1]
                for key in keys:
                    x = ord(key) - ord('a')
                    if (st >> x & 1) == 0:
                        for i in range(len(pos)):
                            if key in path_info[pos[i]].keys():
                                cost, path = path_info[pos[i]][key]
                                if all(st >> (ord(ch.lower()) - ord('a')) & 1 for ch in path):
                                    new_dis = dis + cost
                                    new_pos = pos.copy()
                                    new_pos[i] = key
                                    new_tp = tuple(new_pos + [st | 1 << x])
                                    if new_tp not in g_mp.keys() or new_dis < g_mp[new_tp]:
                                        g_mp[new_tp] = new_dis
            f_mp = g_mp
        return min(f_mp.values())

    def solve_part_1(self):
        mp = [list(s) for s in self.mp]
        for i in range(len(mp)):
            for j in range(len(mp[0])):
                if mp[i][j] == '@':
                    mp[i][j] = '0'
        return self._run(mp)

    def solve_part_2(self):
        mp = [list(s) for s in self.mp]
        for i in range(len(mp)):
            for j in range(len(mp[0])):
                if mp[i][j] == '@':
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx == 0 or dy == 0:
                                mp[i + dx][j + dy] = '#'
                            else:
                                mp[i + dx][j + dy] = {(-1, -1): '0', (-1, 1): '1', (1, -1): '2', (1, 1): '3'}[(dx, dy)]
        return self._run(mp)


if __name__ == "__main__":
    src = get_data(Solver2019Day18.YEAR, Solver2019Day18.DAY)
    sol = Solver2019Day18(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

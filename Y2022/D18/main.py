from utils import Solver, get_data
from collections import defaultdict, deque


class Solver2022Day18(Solver):
    YEAR = 2022
    DAY = 18

    def __init__(self, src):
        self.cubes = [tuple(map(int, s.split(','))) for s in src.strip().split()]

    dirs = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

    def solve_part_1(self):
        st = set(self.cubes)
        ans = len(st) * 6
        cnt = 0
        for tp in st:
            for dir in self.dirs:
                tq = tuple(t + d for t, d in zip(tp, dir))
                if tq in st:
                    cnt += 1
        return ans - cnt

    def solve_part_2(self):
        cubes = self.cubes
        mnx, mny, mnz = min(v[0] for v in cubes) - 1, min(v[1] for v in cubes) - 1, min(v[2] for v in cubes) - 1
        mxx, mxy, mxz = max(v[0] for v in cubes) + 1, max(v[1] for v in cubes) + 1, max(v[2] for v in cubes) + 1
        mp = defaultdict(int)
        for tp in cubes:
            mp[tp] = 2
        q = deque([(mnx, mny, mnz)])
        ans = 0
        while len(q) > 0:
            sx, sy, sz = q.popleft()
            for dx, dy, dz in self.dirs:
                x, y, z = sx + dx, sy + dy, sz + dz
                if mnx <= x <= mxx and mny <= y <= mxy and mnz <= z <= mxz:
                    if mp[x, y, z] == 2:
                        ans += 1
                    elif mp[x, y, z] == 0:
                        mp[x, y, z] = 1
                        q.append((x, y, z))
        return ans


if __name__ == "__main__":
    src = get_data(Solver2022Day18.YEAR, Solver2022Day18.DAY)
    sol = Solver2022Day18(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

import re
from utils import Solver, get_data
from typing import NamedTuple


class V(NamedTuple('V', [('x', int), ('y', int), ('z', int)])):
    def __add__(self, other: 'V') -> 'V':
        return V(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'V') -> 'V':
        return V(self.x - other.x, self.y - other.y, self.z - other.z)

    def __xor__(self, other: 'V') -> 'V':  # cross product
        return V(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                 self.x * other.y - self.y * other.x)

    def __mul__(self, k: int):
        return V(self.x * k, self.y * k, self.z * k)

    def dot(self, other: 'V'):
        return self.x * other.x + self.y * other.y + self.z * other.z


class Solver2022Day22(Solver):
    YEAR = 2022
    DAY = 22

    def __init__(self, src):
        mp, op_str = src.strip('\n').split('\n\n')
        self.ops = [int(s) if s.isdigit() else s for s in re.findall(r'\d+|[A-Za-z]', op_str)]
        self.mp = mp.split('\n')

    def is_space(self, x, y):
        return 0 <= x < len(self.mp) and 0 <= y < len(self.mp[x]) and self.mp[x][y] != ' '

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def _run(self, nxt):
        x, y, p = 0, self.mp[0].find('.'), 0
        for op in self.ops:
            if isinstance(op, int):
                for _ in range(op):
                    nx, ny, np = nxt[x][y][p]
                    if self.mp[nx][ny] == '#':
                        break
                    x, y, p = nx, ny, np
            elif op == 'L':
                p = (p - 1) % len(self.dirs)
            else:
                p = (p + 1) % len(self.dirs)
        return 1000 * (x + 1) + 4 * (y + 1) + p

    def solve_part_1(self):
        n, m = len(self.mp), max(len(s) for s in self.mp)
        nxt = [[[None] * 4 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not self.is_space(i, j):
                    continue
                for p, (dx, dy) in enumerate(self.dirs):
                    x, y = i, j
                    while True:
                        x, y = (x + dx) % n, (y + dy) % m
                        if self.is_space(x, y):
                            nxt[i][j][p] = [x, y, p]
                            break
        return self._run(nxt)

    def solve_part_2(self):
        # https://topaz.github.io/paste/#XQAAAQCUDAAAAAAAAAAzHIoib6pENkSmUIKIED8dy140D1lKWSKhzWZruQROc6UAsbIcPuPN/71ynNCRGTFEFKUEjTCwuAcxmuK2rk4iU4QUDIxfvX32iOSohH/i4c0EO7BEKb2VM699CPBK2pDGBSn4qHGCb+xT8pXkyXk1d0fjGX8Kwz6sicv/PyuMp3eoGHPqXYBOdJO5Hh/974zFt5BKuhdC1CgTWgWEJVghZwbjT7mbFtZce3ytK488tT6UZ/hASBw6jJ33jOjuG/SqTQSIzHSqQ2coxMIuXmqzctg4BPhWto68HVdPd7E1+AerymSV7RnLpITRlGfWG1D2dxvAEnC3NrTzDHtJ/gnOt4+LtfRLikXYAqJFOoVvzYntDOd9MBfRa1I/0zvUHqGM+O0FHkprE4Zyv+Z1Dm/kKKpfGy4QKTHcwNIN5j6R1fcQbtGk4HrLqtEeS9WXI4tGM4yyG1L5cFjExf5/+2CuOy9zlD9t6X/Qp5fZWiDmxRHXOLRvK5fA000bUPKm4qSPIesyiPCg4c5uknV/dnn9Sz8ryDRw5XmZrRinHJrq68FMM0LGcoExLBXjU8f1L5Lj5XRDQU3tQ4bZ5HwZX9OvrktzLueHJOrG7Do0EF1UJ0pgnFDrxi1k87VKTaIRW9EKHyW1fHXOgyTCLNqBthlhr12ajq+VSMtefg7RxRNVQxQE4NBQ+SL0/plazRvtIHZhAuYJAxjKPbo5sH5oDh3FYeZCRQlvJMCzckViev4mAAFFF969JJKtmHAiCUb81gY53JA0JchbsTqy7M2dXieVRZV2TEXB/6lVN+/F8WfBjxfmWZCa/xJMktK5BfmmrHTg6F70QJCwPFj0vFEyYnZAZGILSP6uI3SCod0bMWo4h5IBpRiDg8FcHDCfUwKD+sENfUF04vdYeBKMNVgVhC4LIsGMswVyzpjkdyQN2+LZ5Od0n+Hi//y4NQ4GFfzVRsp5FxJubNSZJTJrFG0DODhFmsbF8nSixR7ASHRtdFgwoztG0q97HjVJiLTK83nEYH+PnjpsCj0ACPhECLkuUcdWMAZ4FBQMYdBbaRn4i7gKv4NXM1VX9p3ztRbW45LqGLj5iRrctiF1dsgYJ+zlyLuwWmxpiPRc8l2pmu4hgmZiTTjXP7Nk+MRGYRkCPkAaHLZBkhPtz+FC3qP5mAFAq9xopRrr1Fmj/MRQIR+eDbkR+JSRwg/tKyGgHyHBM9feKHziflenqmgHwmBrjnR3AcYxqvPPmQZaQ5OFeV30/5vfRFTg2qukpyiWAdMIio2N7tG/oOIvkcK/pwr/rAJKX+E4T0ljPjLRZqn/4MdD1Fa7r57DWcuNfudcMoRbM0PGUBPE5Z0T+lri8wxwXpVEIz8z9epJEw4Q8r0cd6sCp29F+Z0kwadm7JCx5MMBH4gsGam6IF1FUpB35EuhoJ5LBkWfASn1DtlWF9OnWnnnWB4B2fo2JbKICojSIVQnBmIzsLkh/t3JwyGRxSPw8GCS370n4lEWb12+YvIZeb/N4d1TP0BDXoxD/8qvt/Y=
        n, m = len(self.mp), max(len(s) for s in self.mp)
        M = round((sum(sum(ch in ".#" for ch in s) for s in self.mp) // 6) ** 0.5)
        faces, edges = dict(), dict()

        def dfs(i: int, j: int, xyz: V, di: V, dj: V):
            if not self.is_space(i, j) or (i, j) in faces:
                return
            faces[(i, j)] = (xyz, di, dj)
            for r in range(M):
                edges[(xyz + di * r, di ^ dj)] = i + r, j
                edges[(xyz + di * r + dj * (M - 1), di ^ dj)] = i + r, j + M - 1
                edges[(xyz + dj * r, di ^ dj)] = i, j + r
                edges[(xyz + dj * r + di * (M - 1), di ^ dj)] = i + M - 1, j + r
            dfs(i + M, j, xyz + di * (M - 1), di ^ dj, dj)
            dfs(i - M, j, xyz + (di ^ dj) * (M - 1), dj ^ di, dj)
            dfs(i, j + M, xyz + dj * (M - 1), di, di ^ dj)
            dfs(i, j - M, xyz + (di ^ dj) * (M - 1), di, dj ^ di)

        x, y = 0, self.mp[0].find('.')
        dfs(x, y, V(0, 0, 0), V(1, 0, 0), V(0, 1, 0))
        nxt = [[[None] * 4 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not self.is_space(i, j):
                    continue
                for p, (dx, dy) in enumerate(self.dirs):
                    x, y = i + dx, j + dy
                    if self.is_space(x, y):
                        nxt[i][j][p] = x, y, p
                    else:
                        xyz, di3, dj3 = faces[(i // M * M, j // M * M)]
                        here = xyz + di3 * (i % M) + dj3 * (j % M)
                        n = di3 ^ dj3
                        nx, ny = edges[(here, di3 * -dx + dj3 * -dy)]
                        _, di3, dj3 = faces[(nx // M * M, ny // M * M)]
                        ex, ey = di3.dot(n), dj3.dot(n)
                        nxt[i][j][p] = nx, ny, self.dirs.index([ex, ey])
        return self._run(nxt)


if __name__ == "__main__":
    src = get_data(Solver2022Day22.YEAR, Solver2022Day22.DAY)
    sol = Solver2022Day22(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

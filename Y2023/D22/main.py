import re
from collections import defaultdict, deque
from typing import NamedTuple
from itertools import product

from utils import Solver, get_data


class Cube(NamedTuple('Cube', [('x1', int), ('x2', int), ('y1', int), ('y2', int), ('z1', int), ('z2', int)])):
    def __and__(self, other):
        c = Cube(max(self.x1, other.x1), min(self.x2, other.x2),
                 max(self.y1, other.y1), min(self.y2, other.y2),
                 max(self.z1, other.z1), min(self.z2, other.z2),
                 )
        if c.x1 <= c.x2 and c.y1 <= c.y2 and c.z1 <= c.z2:
            return c
        return None

    def size(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

    def units(self):
        return list(product(range(self.x1, self.x2 + 1), range(self.y1, self.y2 + 1), range(self.z1, self.z2 + 1)))


class Solver2023Day22(Solver):
    YEAR = 2023
    DAY = 22

    def __init__(self, src):
        pat = re.compile(r"(\d+),(\d)+,(\d+)~(\d+),(\d+),(\d+)")
        self.cubes = []
        for tp in pat.findall(src.strip()):
            self.cubes.append(Cube(int(tp[0]), int(tp[3]), int(tp[1]), int(tp[4]), int(tp[2]), int(tp[5])))
        self.ans1 = self.ans2 = None

    def run(self):
        cubes = sorted(self.cubes, key=lambda c: (c.z1, c.z2))
        mx = defaultdict(lambda: [0, -1])
        support = [[] for _ in range(len(cubes))]
        deg = [0 for _ in range(len(cubes))]
        for v, c in enumerate(cubes):
            info = [mx[x, y] for x, y in product(range(c.x1, c.x2 + 1), range(c.y1, c.y2 + 1))]
            mx_h = max(v[0] for v in info)
            support_set = set(v[1] for v in info if v[0] == mx_h)
            for u in support_set:
                if u != -1:
                    support[u].append(v)
            deg[v] = len(support_set)
            for x, y in product(range(c.x1, c.x2 + 1), range(c.y1, c.y2 + 1)):
                mx[x, y] = [mx_h + c.z2 - c.z1 + 1, v]
        self.ans1 = self.ans2 = 0
        for i in range(len(cubes)):
            if all(deg[j] >= 2 for j in support[i]):
                self.ans1 += 1

        def que(st):
            d = deg.copy()
            q = deque([st])
            cnt = -1
            while len(q) > 0:
                u = q.popleft()
                cnt += 1
                for v in support[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        q.append(v)
            return cnt

        self.ans2 = sum(que(st) for st in range(len(cubes)))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2023Day22.YEAR, Solver2023Day22.DAY)
    sol = Solver2023Day22(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

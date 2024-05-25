import re
from collections import defaultdict

from utils import Solver, get_data

from typing import NamedTuple


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


class Solver2021Day22(Solver):
    YEAR = 2021
    DAY = 22

    def __init__(self, src):
        pat = re.compile(r'(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)')
        self.ops = [[tp[0], Cube(*map(int, tp[1:]))] for tp in pat.findall(src.strip())]

    def _run(self, scope=None):
        mp = defaultdict(int)
        for op, cube in self.ops:
            mq = mp.copy()
            if scope and (cube := cube & scope) is None:
                continue
            for pre_cube, val in mp.items():
                if inter := pre_cube & cube:
                    mq[inter] -= val
            if op == 'on':
                mq[cube] += 1
            mp = mq
        return sum(cube.size() * v for cube, v in mp.items())

    def solve_part_1(self):
        return self._run(Cube(-50, 50, -50, 50, -50, 50))

    def solve_part_2(self):
        return self._run()


if __name__ == "__main__":
    src = get_data(Solver2021Day22.YEAR, Solver2021Day22.DAY)
    sol = Solver2021Day22(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

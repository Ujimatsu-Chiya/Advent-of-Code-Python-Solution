import re
from collections import namedtuple, defaultdict
from functools import lru_cache
from heapq import heappush, heappop
from typing import NamedTuple

from utils import Solver, get_data

ROCKY, WET, NARROW = range(3)
CLIMBING_GEAR, TORCH, NEITHER = range(3)
COMPATIBILITY = {ROCKY: {CLIMBING_GEAR, TORCH},
                 WET: {CLIMBING_GEAR, NEITHER},
                 NARROW: {TORCH, NEITHER}}


class State(NamedTuple):
    region: tuple
    equipment: int


class Cave:
    def __init__(self, depth, target):
        self.depth = depth
        self.target = target

    @lru_cache(maxsize=None)
    def geologic_index(self, region):
        x, y = region
        if region == (0, 0) or region == self.target:
            return 0
        elif y == 0:
            return x * 16807
        elif x == 0:
            return y * 48271
        else:
            return self.erosion_level((x - 1, y)) * self.erosion_level((x, y - 1))

    def erosion_level(self, region):
        return (self.geologic_index(region) + self.depth) % 20183

    def cal_type(self, region):
        return self.erosion_level(region) % 3

    def cal_g(self, st):
        return abs(self.target[0] - st.region[0]) + abs(self.target[1] - st.region[1]) + (
            7 if st.equipment != TORCH else 0)

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def next_state(self, st):
        for dx, dy in self.dirs:
            new_pos = (st.region[0] + dx, st.region[1] + dy)
            if new_pos[0] >= 0 and new_pos[1] >= 0 and st.equipment in COMPATIBILITY[self.cal_type(new_pos)]:
                yield State(new_pos, st.equipment), 1
        for equip in range(3):
            if equip != st.equipment and equip in COMPATIBILITY[self.cal_type(st.region)]:
                yield State(st.region, equip), 7

    def explore(self):
        f = defaultdict(lambda: float('inf'))
        init = State((0, 0), TORCH)
        ed = State(self.target, TORCH)
        t = (self.cal_g(init) + 0, 0, init)
        q = []
        heappush(q, t)
        while len(q) > 0:
            t, f_val, st = heappop(q)
            if st in f.keys():
                continue
            f[st] = f_val
            if st == ed:
                break
            for new_st, cost in self.next_state(st):
                if new_st not in f.keys():
                    heappush(q, (self.cal_g(new_st) + f_val + cost, f_val + cost, new_st))
        return f[ed]


class Solver2018Day22(Solver):
    YEAR = 2018
    DAY = 22

    def __init__(self, src):
        pat = re.compile(r"(\d+)")
        self.d, self.n, self.m = list(map(int, pat.findall(src.strip())))
        self.ans1 = self.ans2 = None

    def run(self):
        cave = Cave(self.d, (self.n, self.m))
        self.ans1 = sum(cave.cal_type((i, j)) for i in range(self.n + 1) for j in range(self.m + 1))
        self.ans2 = cave.explore()

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day22.YEAR, Solver2018Day22.DAY)
    sol = Solver2018Day22(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

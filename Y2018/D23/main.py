from math import ceil, log2
import re
from heapq import heappush, heappop

from utils import Solver, get_data


class Solver2018Day23(Solver):
    YEAR = 2018
    DAY = 23

    def __init__(self, src):
        pat = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")
        self.bots = []
        for v in pat.findall(src.strip()):
            self.bots.append(tuple(map(int, v)))

    def solve_part_1(self):
        def dis(p1, p2):
            return sum(abs(x1 - x2) for x1, x2 in zip(p1[:3], p2[:3]))

        ls = self.bots
        choose = max(ls, key=lambda v: v[3])
        return len([bot for bot in self.bots if dis(bot, choose) <= choose[3]])

    def divide_cube(self, x, y, z, sz):
        sz = sz // 2
        for i in range(8):
            yield x + (0 if i & 1 else sz), y + (0 if i & 2 else sz), z + (0 if i & 4 else sz), sz

    def bot_intersect_cube(self, bot, cube):
        r = bot[3]
        sz = cube[3]
        v = 0
        for b, c in zip(bot[:3], cube[:3]):
            if b < c:
                v += c - b
            elif b >= c + sz:
                v += b - c - sz + 1
        return v <= r

    def bots_in_cube(self, cube):
        return sum(1 for bot in self.bots if self.bot_intersect_cube(bot, cube))

    def solve_part_2(self):
        x_list, y_list, z_list, _ = zip(*self.bots)
        max_x, max_y, max_z = max(x_list), max(y_list), max(z_list)
        min_x, min_y, min_z = min(x_list), min(y_list), min(z_list)
        l = max(max_x - min_x, max_y - min_y, max_z - min_z)
        sz = 2 ** (ceil(log2(l)))

        q = []
        heappush(q, (-len(self.bots), sz, abs(min_x) + abs(min_y) + abs(min_z), min_x, min_y, min_z))
        while len(q) > 0:
            _, sz, d, x, y, z = heappop(q)
            if sz == 1:
                return d
            for nx, ny, nz, nsz in self.divide_cube(x, y, z, sz):
                cnt = self.bots_in_cube((nx, ny, nz, nsz))
                if cnt != 0:
                    heappush(q, (-cnt, nsz, abs(nx) + abs(ny) + abs(nz), nx, ny, nz))


if __name__ == "__main__":
    src = get_data(Solver2018Day23.YEAR, Solver2018Day23.DAY)
    sol = Solver2018Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

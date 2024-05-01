import math
import re
from heapq import heappush, heappop

from utils import Solver, get_data


class Solver2018Day23(Solver):
    YEAR = 2018
    DAY = 23

    def parse(self, src):
        pat = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")
        ls = []
        for v in pat.findall(src.strip()):
            ls.append(tuple(map(int, v)))
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        p = max(range(len(ls)), key=lambda index: ls[index][3])

        def dis(p1, p2):
            return sum(abs(x1 - x2) for x1, x2 in zip(p1[:3], p2[:3]))

        ans = 0
        for i in range(len(ls)):
            if dis(ls[i], ls[p]) <= ls[p][3]:
                ans += 1
        return ans

    def is_in_range(self, ax, ay, az, bx, by, bz, r):
        return r >= abs(ax - bx) + abs(ay - by) + abs(az - bz)

    cube_deltas = (
        (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)
    )

    def calculate_initial_search_cube(self, bots):
        max_x = max_y = max_z = -math.inf
        min_x = min_y = min_z = math.inf

        for x, y, z, r in bots:
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            max_z = max(z, max_z)

            min_x = min(x, min_x)
            min_y = min(y, min_y)
            min_z = min(z, min_z)

        min_side_length = max(
            abs(max_x - min_x),
            abs(max_y - min_y),
            abs(max_z - min_z)
        )

        # find a power of two, so subdividing the cube is cleaner
        side_length = 2
        while 1 + side_length < min_side_length:
            side_length *= 2

        return min_x, min_y, min_z, side_length

    def cube_corners(self, x, y, z, sz):
        sz -= 1
        return list((x + (dx * sz), y + (dy * sz), z + (dz * sz))
                    for dx, dy, dz in self.cube_deltas)

    def bot_extremities(self, bot):
        x, y, z, r = bot
        return (
            (x + r, y, z),
            (x - r, y, z),
            (x, y + r, z),
            (x, y - r, z),
            (x, y, z + r),
            (x, y, z - r)
        )

    def subdivide_search_cube(self, x, y, z, sz):
        assert sz != 0, "Cannot subdivide a cube of size 1, I must have broken something"
        sz = sz // 2
        for dx, dy, dz in self.cube_deltas:
            yield x + (sz * dx), y + (sz * dy), z + (sz * dz), sz

    # the following might seem stupid and redundant but they are different
    # - cube_intersects_bot: check if any cube corners are within manhattan range of bot centre
    # - bot_intersects_cube: check if any bot extremities lie within the cube
    def cube_intersects_bot(self, cube, bot):
        bx, by, bz, r = bot
        cx, cy, cz, sz = cube
        for x, y, z in self.cube_corners(cx, cy, cz, sz):
            if self.is_in_range(bx, by, bz, x, y, z, r):
                return True
        return False

    def bot_intersects_cube(self, bot, cube):
        bx, by, bz, r = bot
        cx, cy, cz, sz = cube

        cx_max = cx + sz
        cy_max = cy + sz
        cz_max = cz + sz

        for x, y, z in self.bot_extremities(bot):
            x_inside = cx_max > x >= cx
            y_inside = cy_max > y >= cy
            z_inside = cz_max > z >= cz
            if x_inside and y_inside and z_inside:
                return True

        return False

    def bots_in_cube(self, bots, cube):
        return sum(1 for bot in bots if self.bot_intersects_cube(bot, cube) or self.cube_intersects_bot(cube, bot))

    def add_search_cube(self, queue, nbots, x, y, z, sz):
        heappush(queue, (-nbots, sz, abs(x) + abs(y) + abs(z), x, y, z))

    def solve_part_2(self, src):
        bots = self.parse(src)
        cube = self.calculate_initial_search_cube(bots)

        queue = []
        self.add_search_cube(queue, len(bots), *cube)

        while any(queue):
            bots_in_range, sz, _, x, y, z = heappop(queue)

            if sz == 1:
                return x + y + z

            else:
                for nx, ny, nz, nsz in self.subdivide_search_cube(x, y, z, sz):
                    nb = self.bots_in_cube(bots, (nx, ny, nz, nsz))
                    if nb != 0:
                        self.add_search_cube(queue, nb, nx, ny, nz, nsz)


if __name__ == "__main__":
    sol = Solver2018Day23()
    src = get_data(Solver2018Day23.YEAR, Solver2018Day23.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

import math
from itertools import count

from utils import Solver, get_data


class Solver2017Day3(Solver):
    YEAR = 2017
    DAY = 3

    def __init__(self, src):
        self.n= int(src.strip())

    def solve_part_1(self):
        def spiral_position(n):
            if n == 1:
                return 0, 0

            layer = math.ceil((math.sqrt(n) - 1) / 2)
            pre_num = (2 * layer - 1) ** 2
            side_length = 2 * layer
            steps = n - pre_num - 1
            side = steps // side_length
            offset = steps % side_length
            if side == 0:
                return layer, -layer + offset + 1
            elif side == 1:
                return layer - offset - 1, layer
            elif side == 2:
                return -layer, layer - offset - 1
            else:
                return -layer + offset + 1, -layer

        x, y = spiral_position(self.n)
        return abs(x) + abs(y)

    def solve_part_2(self):
        def gen_pos():
            yield 0, 0
            for layer in count(1):
                side_length = layer * 2
                for offset in range(side_length):
                    yield layer, -layer + offset + 1
                for offset in range(side_length):
                    yield layer - offset - 1, layer
                for offset in range(side_length):
                    yield -layer, layer - offset - 1
                for offset in range(side_length):
                    yield -layer + offset + 1, -layer

        mp = {}
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for x, y in gen_pos():
            if x == y == 0:
                mp[x, y] = 1
            else:
                mp[x, y] = sum(mp.get((x + dx, y + dy), 0) for dx, dy in dirs)
            if mp[x, y] > self.n:
                return mp[x, y]


if __name__ == "__main__":
    src = get_data(Solver2017Day3.YEAR, Solver2017Day3.DAY)
    sol = Solver2017Day3(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

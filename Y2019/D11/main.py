from utils import Solver, get_data
from collections import defaultdict
from tools import IntCodeComputer


class Solver2019Day11(Solver):
    YEAR = 2019
    DAY = 11

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def _run(self, default_func):
        mp = defaultdict(default_func)
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        com = IntCodeComputer(self.ops)
        x, y, p = 0, 0, 0
        while not com.halt:
            c = mp[(x, y)]
            com.add_input(c)
            c, r = com.get_output(), com.get_output()
            mp[(x, y)] = c
            if r == 0:
                p = (p - 1) % 4
            else:
                p = (p + 1) % 4
            x += dirs[p][0]
            y += dirs[p][1]
        return mp

    def solve_part_1(self):
        mp = self._run(int)
        return len(mp)

    def solve_part_2(self):
        mp = self._run(lambda: 1)
        st = {(x, y) for x, y in mp.keys() if mp[(x, y)]}
        x_list, y_list = zip(*st)
        mnx, mxx = min(x_list), max(x_list)
        mny, mxy = min(y_list), max(y_list)
        ans = []
        for i in range(mnx, mxx + 1):
            ans.append("".join('#' if (i, j) in st else ' ' for j in range(mny, mxy + 1)))
        return "\n".join(ans)


if __name__ == "__main__":
    src = get_data(Solver2019Day11.YEAR, Solver2019Day11.DAY)
    sol = Solver2019Day11(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

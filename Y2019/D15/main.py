from collections import deque

from tools import IntCodeComputer, Point
from utils import Solver, get_data


class Solver2019Day15(Solver):
    YEAR = 2019
    DAY = 15

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))
        self.ans1 = self.ans2 = None

    def run(self):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        p = IntCodeComputer(self.ops)
        pt = None
        pt_st = set()

        def dfs(x, y):
            if Point(x, y) in pt_st:
                return
            pt_st.add(Point(x, y))
            for i in range(4):
                p.add_input(i + 1)
                k = p.get_output()
                if k != 0:
                    dfs(x + dirs[i][0], y + dirs[i][1])
                    if k == 2:
                        nonlocal pt
                        pt = Point(x + dirs[i][0], y + dirs[i][1])
                    p.add_input((i ^ 1) + 1)
                    assert p.get_output() != 0

        def bfs(st):
            d = {st: 0}
            q = deque([st])
            while len(q) > 0:
                u = q.popleft()
                for v in u.neighbor4():
                    if v in pt_st and v not in d.keys():
                        d[v] = d[u] + 1
                        q.append(v)
            return d

        dfs(0, 0)
        self.ans1 = bfs(Point(0, 0))[pt]
        self.ans2 = max(bfs(pt).values())

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2019Day15.YEAR, Solver2019Day15.DAY)
    sol = Solver2019Day15(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from utils import Solver, get_data
from tools import Point


class Solver2019Day3(Solver):
    YEAR = 2019
    DAY = 3

    def __init__(self, src):
        a_str, b_str = src.strip().split('\n')
        self.a = [[s[0], int(s[1:])] for s in a_str.split(',')]
        self.b = [[s[0], int(s[1:])] for s in b_str.split(',')]
        self.ans1 = self.ans2 = None

    def run(self):
        def get_mp(path):
            x = y = s = 0
            mp = {}
            dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
            for ch, d in path:
                for _ in range(d):
                    x += dirs[ch][0]
                    y += dirs[ch][1]
                    s += 1
                    mp[Point(x, y)] = s
            return mp

        ma = get_mp(self.a)
        mb = get_mp(self.b)
        self.ans1 = min(p.manhattan_dis() for p in ma.keys() & mb.keys())
        self.ans2 = min(v + mb[k] for k, v in ma.items() if k in mb.keys())

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2019Day3.YEAR, Solver2019Day3.DAY)
    sol = Solver2019Day3(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

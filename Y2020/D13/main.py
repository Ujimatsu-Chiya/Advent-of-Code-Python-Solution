from tools import CRT
from utils import Solver, get_data


class Solver2020Day13(Solver):
    YEAR = 2020
    DAY = 13

    def __init__(self, src):
        s, t = src.strip().split()
        self.tm = int(s)
        self.queries = [int(s) if s != 'x' else -1 for s in t.split(',')]

    def solve_part_1(self):
        vals = [x for x in self.queries if x != -1]
        next_time = lambda x: (self.tm + x - 1) // x * x
        p = min(vals, key=next_time)
        return (next_time(p) - self.tm) * p

    def solve_part_2(self):
        que = [[-i % x, x] for i, x in enumerate(self.queries) if x != -1]
        return CRT(*zip(*que))


if __name__ == "__main__":
    src = get_data(Solver2020Day13.YEAR, Solver2020Day13.DAY)
    sol = Solver2020Day13(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

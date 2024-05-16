from utils import Solver, get_data
from collections import defaultdict
from tools import IntCodeComputer


class Solver2019Day13(Solver):
    YEAR = 2019
    DAY = 13

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def solve_part_1(self):
        p = IntCodeComputer(self.ops)
        a = p.get_all_output()
        mp = defaultdict(int)
        for i in range(0, len(a), 3):
            x, y, tp = a[i], a[i + 1], a[i + 2]
            mp[(x, y)] = tp
        return list(mp.values()).count(2)

    def solve_part_2(self):
        p = IntCodeComputer(self.ops)
        p.ops[0] = 2
        a = p.get_all_output()
        ans = 0
        bx = px = 0
        while not p.halt:
            inp = 1 if bx > px else -1 if bx < px else 0
            p.add_input(inp)
            a += p.get_all_output()
            for i in range(0, len(a), 3):
                if a[i] == -1 and a[i + 1] == 0:
                    ans = a[i + 2]
                elif a[i + 2] == 3:
                    px = a[i]
                elif a[i + 2] == 4:
                    bx = a[i]
                else:
                    assert 0 <= a[i + 2] < 5
        return ans


if __name__ == "__main__":
    src = get_data(Solver2019Day13.YEAR, Solver2019Day13.DAY)
    sol = Solver2019Day13(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

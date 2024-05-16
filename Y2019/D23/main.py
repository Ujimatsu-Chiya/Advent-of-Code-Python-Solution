from tools import IntCodeComputer
from utils import Solver, get_data
from itertools import count


class Solver2019Day23(Solver):
    YEAR = 2019
    DAY = 23

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))
        self.ans1 = self.ans2 = None

    def run(self):
        M = 50
        pre = now = None
        p_list = [IntCodeComputer(self.ops, [i]) for i in range(M)]
        while True:
            idle = True
            for i, p in enumerate(p_list):
                ls = p.get_all_output()
                if len(ls) > 0:
                    for i in range(0, len(ls), 3):
                        id, x, y = ls[i:i + 3]
                        if id == 255:
                            now = [x, y]
                            if self.ans1 is None:
                                self.ans1 = y
                        else:
                            p_list[id].add_list_input([x, y])
                    idle = False
                else:
                    p.add_input(-1)

            if idle and now:
                p_list[0].add_list_input(now)
                if pre and pre[1] == now[1]:
                    self.ans2 = now[1]
                    return
                pre = now


    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2019Day23.YEAR, Solver2019Day23.DAY)
    sol = Solver2019Day23(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from utils import Solver, get_data
from tools import IntCodeComputer


class Solver2019Day5(Solver):
    YEAR = 2019
    DAY = 5

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def solve_part_1(self):
        p = IntCodeComputer(self.ops, [1])
        return p.get_all_output()[-1]

    def solve_part_2(self):
        p = IntCodeComputer(self.ops, [5])
        return p.get_all_output()[-1]


if __name__ == "__main__":
    src = get_data(Solver2019Day5.YEAR, Solver2019Day5.DAY)
    sol = Solver2019Day5(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

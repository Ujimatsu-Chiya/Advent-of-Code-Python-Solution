from tools import IntCodeComputer
from utils import Solver, get_data


class Solver2019Day9(Solver):
    YEAR = 2019
    DAY = 9

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def solve_part_1(self):
        p = IntCodeComputer(self.ops, [1])
        return p.get_all_output()[-1]

    def solve_part_2(self):
        p = IntCodeComputer(self.ops, [2])
        return p.get_all_output()[-1]


if __name__ == "__main__":
    src = get_data(Solver2019Day9.YEAR, Solver2019Day9.DAY)
    sol = Solver2019Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

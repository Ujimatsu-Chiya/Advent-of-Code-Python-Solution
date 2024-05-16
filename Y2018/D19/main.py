import re

from tools import divisors_sigma
from utils import Solver, get_data


class Solver2018Day19(Solver):
    YEAR = 2018
    DAY = 19

    def __init__(self, src):
        pat1 = re.compile(r'(\w+) (\d+) (\d+) (\d+)')
        self.ops = []
        for tp in pat1.findall(src.strip()):
            self.ops.append([tp[0]] + list(map(int, tp[1:])))
        pat2 = re.compile(r'#ip (\d+)')
        self.ip = int(pat2.findall(src.strip())[0])

    def solve_part_1(self):
        x = self.ops[21][2]
        y = self.ops[23][2]
        return divisors_sigma(x * 22 + y + 836)

    def solve_part_2(self):
        x = self.ops[21][2]
        y = self.ops[23][2]
        return divisors_sigma(x * 22 + y + 10551236)


if __name__ == "__main__":
    src = get_data(Solver2018Day19.YEAR, Solver2018Day19.DAY)
    sol = Solver2018Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

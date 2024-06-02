import re

from utils import Solver, get_data


class Solver2022Day4(Solver):
    YEAR = 2022
    DAY = 4

    def __init__(self, src):
        pat = re.compile(r'(\d+)-(\d+),?(\d+)-(\d+)?')
        self.queries = [[(int(v[0]), int(v[1])), (int(v[2]), int(v[3]))] for v in pat.findall(src.strip())]

    def solve_part_1(self):
        return sum(1 for v in self.queries if v[0][0] <= v[1][0] and v[1][1] <= v[0][1] or
                   v[1][0] <= v[0][0] and v[0][1] <= v[1][1])

    def solve_part_2(self):
        return sum(1 for v in self.queries if not(v[0][1] < v[1][0] or v[1][1] < v[0][0]))


if __name__ == "__main__":
    src = get_data(Solver2022Day4.YEAR, Solver2022Day4.DAY)
    sol = Solver2022Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from utils import Solver, get_data


class Solver2022Day1(Solver):
    YEAR = 2022
    DAY = 1

    def __init__(self, src):
        self.queries = [list(map(int,s.split())) for s in src.strip().split('\n\n')]

    def solve_part_1(self):
        return max(sum(v) for v in self.queries)

    def solve_part_2(self):
        return sum(sorted(sum(v) for v in self.queries)[-3:])


if __name__ == "__main__":
    src = get_data(Solver2022Day1.YEAR, Solver2022Day1.DAY)
    sol = Solver2022Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
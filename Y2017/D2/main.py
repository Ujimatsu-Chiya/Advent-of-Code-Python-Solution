from utils import Solver, get_data


class Solver2017Day2(Solver):
    YEAR = 2017
    DAY = 2

    def __init__(self, src):
        self.queries = [list(map(int, s.split())) for s in src.strip().split('\n')]

    def solve_part_1(self):
        return sum(max(v) - min(v) for v in self.queries)

    def solve_part_2(self):
        ans = 0
        for v in self.queries:
            for x in v:
                for y in v:
                    if y > x and y % x == 0:
                        ans += y // x
        return ans


if __name__ == "__main__":
    src = get_data(Solver2017Day2.YEAR, Solver2017Day2.DAY)
    sol = Solver2017Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

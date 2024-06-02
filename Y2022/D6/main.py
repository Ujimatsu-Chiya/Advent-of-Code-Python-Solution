from utils import Solver, get_data


class Solver2022Day6(Solver):
    YEAR = 2022
    DAY = 6

    def __init__(self, src):
        self.s = src.strip()

    def _run(self, M):
        return next(i for i in range(len(self.s) + 1 - M) if len(set(self.s[i:i + M])) == M) + M
    def solve_part_1(self):
        return self._run(4)

    def solve_part_2(self):
        return self._run(14)


if __name__ == "__main__":
    src = get_data(Solver2022Day6.YEAR, Solver2022Day6.DAY)
    sol = Solver2022Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
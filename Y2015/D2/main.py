from utils import Solver, get_data


class Solver2015Day2(Solver):
    YEAR = 2015
    DAY = 2

    def __init__(self, src):
        self.queries = [list(map(int, s.split('x'))) for s in src.strip().split('\n')]

    def solve_part_1(self):
        ls = self.queries
        ans = 0
        for u in ls:
            u.sort()
            ans += 3 * u[0] * u[1] + 2 * (u[0] + u[1]) * u[2]
        return ans

    def solve_part_2(self):
        ls = self.queries
        ans = 0
        for u in ls:
            u.sort()
            ans += 2 * (u[0] + u[1]) + u[0] * u[1] * u[2]
        return ans


if __name__ == "__main__":
    src = get_data(Solver2015Day2.YEAR, Solver2015Day2.DAY)
    sol = Solver2015Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from utils import Solver, get_data


class Solver2015Day2(Solver):
    YEAR = 2015
    DAY = 2

    def parse(self, src):
        return [list(map(int, s.split('x'))) for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for u in ls:
            u.sort()
            ans += 3 * u[0] * u[1] + 2 * (u[0] + u[1]) * u[2]
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for u in ls:
            u.sort()
            ans += 2 * (u[0] + u[1]) + u[0] * u[1] * u[2]
        return ans


if __name__ == "__main__":
    sol = Solver2015Day2()
    src = get_data(Solver2015Day2.YEAR, Solver2015Day2.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

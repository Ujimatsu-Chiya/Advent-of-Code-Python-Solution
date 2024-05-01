from utils import Solver, get_data


class Solver2017Day2(Solver):
    YEAR = 2017
    DAY = 2

    def parse(self, src):
        return [list(map(int,s.split())) for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        a = self.parse(src)
        return sum(max(v) - min(v) for v in a)

    def solve_part_2(self, src):
        a = self.parse(src)
        ans = 0
        for v in a:
            for x in v:
                for y in v:
                    if y > x and y % x == 0:
                        ans += y // x
        return ans


if __name__ == "__main__":
    sol = Solver2017Day2()
    src = get_data(Solver2017Day2.YEAR, Solver2017Day2.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

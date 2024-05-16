from utils import Solver, get_data


class Solver2016Day3(Solver):
    YEAR = 2016
    DAY = 3

    def __init__(self, src):
        self.queries = [list(map(int, s.split())) for s in src.strip().split('\n')]

    def solve_part_1(self):
        ans = 0
        for v in self.queries:
            x, y, z = sorted(v)
            if x + y > z:
                ans += 1
        return ans

    def solve_part_2(self):
        ans = 0
        for i in range(0, len(self.queries), 3):
            for j in range(3):
                x, y, z = sorted([self.queries[i + k][j] for k in range(3)])
                if x + y > z:
                    ans += 1
        return ans


if __name__ == "__main__":
    src = get_data(Solver2016Day3.YEAR, Solver2016Day3.DAY)
    sol = Solver2016Day3(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

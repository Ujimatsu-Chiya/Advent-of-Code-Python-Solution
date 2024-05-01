from utils import Solver, get_data


class Solver2016Day3(Solver):
    YEAR = 2016
    DAY = 3

    def parse(self, src):
        return [list(map(int, s.split())) for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for v in ls:
            x, y, z = sorted(v)
            if x + y > z:
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for i in range(0, len(ls), 3):
            for j in range(3):
                x, y, z = sorted([ls[i + k][j] for k in range(3)])
                if x + y > z:
                    ans += 1
        return ans


if __name__ == "__main__":
    sol = Solver2016Day3()
    src = get_data(Solver2016Day3.YEAR, Solver2016Day3.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

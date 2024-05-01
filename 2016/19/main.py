from utils import Solver, get_data


class Solver2016Day19(Solver):
    YEAR = 2016
    DAY = 19

    def parse(self, src):
        return int(src.strip())

    def solve_part_1(self, src):
        # https://oeis.org/A006257
        n = self.parse(src)

        def cal(n):
            if n == 1:
                return 1
            elif n % 2 == 0:
                return cal(n // 2) * 2 - 1
            else:
                return cal(n // 2) * 2 + 1

        return cal(n)

    def solve_part_2(self, src):
        # https://oeis.org/A334473
        n = self.parse(src)
        k = 0
        while 3 ** (k + 1) <= n:
            k += 1
        b = n - 3 ** k
        if b == 0:
            return n
        elif 3 ** k + b <= 2 * 3 ** k:
            return b
        else:
            return 2 * b - 3 ** k


if __name__ == "__main__":
    sol = Solver2016Day19()
    src = get_data(Solver2016Day19.YEAR, Solver2016Day19.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

from utils import Solver, get_data


class Solver2016Day19(Solver):
    YEAR = 2016
    DAY = 19

    def __init__(self, src):
        self.n = int(src.strip())

    def solve_part_1(self):
        # https://oeis.org/A006257
        def cal(n):
            if n == 1:
                return 1
            elif n % 2 == 0:
                return cal(n // 2) * 2 - 1
            else:
                return cal(n // 2) * 2 + 1

        return cal(self.n)

    def solve_part_2(self):
        # https://oeis.org/A334473
        n = self.n
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
    src = get_data(Solver2016Day19.YEAR, Solver2016Day19.DAY)
    sol = Solver2016Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

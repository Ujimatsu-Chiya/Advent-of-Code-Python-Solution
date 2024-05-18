from utils import Solver, get_data


class Solver2020Day10(Solver):
    YEAR = 2020
    DAY = 10

    def __init__(self, src):
        self.a = list(map(int, src.split()))

    def solve_part_1(self):
        a = [0] + sorted(self.a)
        d = [a[i] - a[i - 1] for i in range(1, len(a))] + [3]
        return d.count(1) * d.count(3)

    def solve_part_2(self):
        a = [0] + sorted(self.a) + [max(self.a) + 3]
        n = len(a)
        f = [0 for _ in range(n)]
        f[0] = 1
        for i in range(1, n):
            for j in range(max(i - 3, 0), i):
                if a[i] - a[j] <= 3:
                    f[i] += f[j]
        return f[-1]


if __name__ == "__main__":
    src = get_data(Solver2020Day10.YEAR, Solver2020Day10.DAY)
    sol = Solver2020Day10(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

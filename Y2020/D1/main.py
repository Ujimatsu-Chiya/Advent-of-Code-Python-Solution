from utils import Solver, get_data


class Solver2020Day1(Solver):
    YEAR = 2020
    DAY = 1

    def __init__(self, src):
        self.a = list(map(int, src.strip().split()))

    def solve_part_1(self):
        M = 2020
        if M % 2 == 0 and self.a.count(M // 2) >= 2:
            return M * M // 4
        st = set(self.a)
        for x in st:
            if M - x in st:
                return x * (M - x)

    def solve_part_2(self):
        a = sorted(self.a)
        n = len(a)
        M = 2020
        for j in range(n):
            k = n - 1
            for i in range(j):
                while k > j and a[i] + a[j] + a[k] > M:
                    k -= 1
                if k > j and a[i] + a[j] + a[k] == M:
                    return a[i] * a[j] * a[k]


if __name__ == "__main__":
    src = get_data(Solver2020Day1.YEAR, Solver2020Day1.DAY)
    sol = Solver2020Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

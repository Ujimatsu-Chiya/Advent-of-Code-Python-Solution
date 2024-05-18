from utils import Solver, get_data


class Solver2020Day9(Solver):
    YEAR = 2020
    DAY = 9

    def __init__(self, src):
        self.a = list(map(int, src.strip().split()))
        self.ans1 = self.ans2 = None

    def run(self):
        n = len(self.a)
        M = 25
        for i in range(M, n):
            if all(self.a[i - M + j] + self.a[i - M + k] != self.a[i] for j in range(M) for k in range(j)):
                self.ans1 = self.a[i]
                break
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += self.a[j]
                if s == self.ans1 and j - i > 0:
                    self.ans2 = min(self.a[i:j+1]) + max(self.a[i:j+1])

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2020Day9.YEAR, Solver2020Day9.DAY)
    sol = Solver2020Day9(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

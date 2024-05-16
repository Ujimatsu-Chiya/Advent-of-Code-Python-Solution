from utils import Solver, get_data


class Solver2018Day11(Solver):
    YEAR = 2018
    DAY = 11

    def __init__(self, src):
        self.n = int(src.strip())
        self.ans1 = self.ans2 = None

    def run(self):
        m = 300
        s = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        for y in range(1, m + 1):
            for x in range(1, m + 1):
                id = x + 10
                w = (id * y + self.n) * id // 100 % 10 - 5
                s[y][x] = s[y - 1][x] + s[y][x - 1] - s[y - 1][x - 1] + w

        def que(i, j, k):
            return s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k]

        mx = max(que(i, j, 3) for i in range(3, m + 1) for j in range(3, m + 1))
        pos = [(j - 2, i - 2) for i in range(3, m + 1) for j in range(3, m + 1) if que(i, j, 3) == mx]
        self.ans1 = ",".join(map(str, pos[0]))
        mx = max(que(i, j, k) for k in range(1, m + 1) for i in range(k, m + 1) for j in range(k, m + 1))
        pos = [(j - k + 1, i - k + 1, k) for k in range(1, m + 1) for i in range(k, m + 1) for j in range(k, m + 1) if
               que(i, j, k) == mx]
        self.ans2 = ",".join(map(str, pos[0]))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day11.YEAR, Solver2018Day11.DAY)
    sol = Solver2018Day11(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

from utils import Solver, get_data


class Solver2017Day17(Solver):
    YEAR = 2017
    DAY = 17

    def __init__(self, src):
        self.n = int(src.strip())

    def solve_part_1(self):
        M = 2017
        a = [0]
        p = 0
        for i in range(1, M + 1):
            p = (p + self.n) % len(a)
            a = a[:p + 1] + [i] + a[p + 1:]
            p += 1
        p = a.index(M)
        return a[(p + 1) % len(a)]

    def solve_part_2(self):
        M = 50000000
        cur = 1
        pos = ans = 0
        for i in range(M):
            to_ins = i + 1
            new = (pos + self.n) % cur
            new += 1
            if new == 1:
                ans = to_ins
            pos = new
            cur += 1
        return ans


if __name__ == "__main__":
    src = get_data(Solver2017Day17.YEAR, Solver2017Day17.DAY)
    sol = Solver2017Day17(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

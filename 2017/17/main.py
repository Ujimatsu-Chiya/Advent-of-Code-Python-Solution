from utils import Solver, get_data


class Solver2017Day17(Solver):
    YEAR = 2017
    DAY = 17

    def parse(self, src):
        return int(src.strip())

    def solve_part_1(self, src):
        n = self.parse(src)
        M = 2017
        a = [0]
        p = 0
        for i in range(1, M + 1):
            p = (p + n) % len(a)
            a = a[:p + 1] + [i] + a[p + 1:]
            p += 1
        p = a.index(M)
        return a[(p + 1) % len(a)]

    def solve_part_2(self, src):
        n = self.parse(src)
        M = 50000000
        cur = 1
        pos = ans = 0
        for i in range(M):
            to_ins = i + 1
            new = (pos + n) % cur
            new += 1
            if new == 1:
                ans = to_ins
            pos = new
            cur += 1
        return ans

if __name__ == "__main__":
    sol = Solver2017Day17()
    src = get_data(Solver2017Day17.YEAR, Solver2017Day17.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
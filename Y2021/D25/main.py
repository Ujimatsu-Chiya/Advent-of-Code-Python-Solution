from utils import Solver, get_data
from itertools import count


class Solver2021Day25(Solver):
    YEAR = 2021
    DAY = 25

    def __init__(self, src):
        self.mp = [[{".": 0, ">": 1, "v": 2}[ch] for ch in s] for s in src.strip().split()]

    def solve_part_1(self):
        mp = self.mp
        n, m = len(mp), len(mp[0])
        for r in count(1):
            s = 0
            for i in range(n):
                ok = [False for _ in range(m)]
                for j in range(m):
                    if mp[i][j] == 1 and mp[i][(j + 1) % m] == 0:
                        ok[j] = True
                for j in range(m):
                    if ok[j]:
                        mp[i][j], mp[i][(j + 1) % m] = 0, 1
                s += sum(ok)
            for j in range(m):
                ok = [False for _ in range(n)]
                for i in range(n):
                    if mp[i][j] == 2 and mp[(i + 1) % n][j] == 0:
                        ok[i] = True
                for i in range(n):
                    if ok[i]:
                        mp[i][j], mp[(i + 1) % n][j] = 0, 2
                s += sum(ok)
            if s == 0:
                return r

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2021Day25.YEAR, Solver2021Day25.DAY)
    sol = Solver2021Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

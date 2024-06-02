from utils import Solver, get_data
from tools import transpose_str


class Solver2023Day13(Solver):
    YEAR = 2023
    DAY = 13

    def __init__(self, src):
        self.mats = [s.split() for s in src.strip().split('\n\n')]

    def solve_part_1(self):
        ans = 0
        for mp in self.mats:
            n, m = len(mp), len(mp[0])
            for i in range(1, n):
                sz = min(i, n - i)
                if mp[i - sz:i] == list(reversed(mp[i:i + sz])):
                    ans += i * 100
            mp = transpose_str(mp)
            for i in range(1, m):
                sz = min(i, m - i)
                if mp[i - sz:i] == list(reversed(mp[i:i + sz])):
                    ans += i
        return ans

    def solve_part_2(self):
        def check(m1, m2):
            ans = 0
            for i in range(len(m1)):
                for j in range(len(m1[0])):
                    if m1[i][j] != m2[i][j]:
                        ans += 1
            return ans == 1

        ans = 0
        for mp in self.mats:
            n, m = len(mp), len(mp[0])
            for i in range(1, n):
                sz = min(i, n - i)
                if check(mp[i - sz:i], list(reversed(mp[i:i + sz]))):
                    ans += i * 100
            mp = transpose_str(mp)
            for i in range(1, m):
                sz = min(i, m - i)
                if check(mp[i - sz:i], list(reversed(mp[i:i + sz]))):
                    ans += i
        return ans


if __name__ == "__main__":
    src = get_data(Solver2023Day13.YEAR, Solver2023Day13.DAY)
    sol = Solver2023Day13(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

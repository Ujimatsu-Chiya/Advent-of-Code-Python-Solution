from collections import Counter

from utils import Solver, get_data


class Solver2016Day6(Solver):
    YEAR = 2016
    DAY = 6

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        n, m = len(ls), len(ls[0])
        ans = ''
        for j in range(m):
            c = Counter(ls[i][j] for i in range(n))
            ch = max(c, key=c.get)
            ans += ch
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        n, m = len(ls), len(ls[0])
        ans = ''
        for j in range(m):
            c = Counter(ls[i][j] for i in range(n))
            ch = min(c, key=c.get)
            ans += ch
        return ans


if __name__ == "__main__":
    sol = Solver2016Day6()
    src = get_data(Solver2016Day6.YEAR, Solver2016Day6.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

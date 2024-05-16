from utils import Solver, get_data


class Solver2015Day1(Solver):
    YEAR = 2015
    DAY = 1

    def __init__(self, src):
        self.queries = src.strip().split()

    def solve_part_1(self):
        ans = 0
        for s in self.queries:
            ans += s.count('(') - s.count(')')
        return ans

    def solve_part_2(self):
        ans = 0
        for s in self.queries:
            f = 0
            for i, ch in enumerate(s):
                f += 1 if ch == '(' else -1
                if f == -1:
                    ans += i + 1
                    break
        return ans


if __name__ == "__main__":
    src = get_data(Solver2015Day1.YEAR, Solver2015Day1.DAY)
    sol = Solver2015Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

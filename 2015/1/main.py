from utils import Solver, get_data


class Solver2015Day1(Solver):
    YEAR = 2015
    DAY = 1

    def parse(self, src):
        ls = src.strip().split()
        return ls

    def solve_part_1(self, src):
        ans = 0
        for s in self.parse(src):
            ans += s.count('(') - s.count(')')
        return ans

    def solve_part_2(self, src):
        ans = 0
        for s in self.parse(src):
            f = 0
            for i, ch in enumerate(s):
                f += 1 if ch == '(' else -1
                if f == -1:
                    ans += i + 1
                    break
        return ans


if __name__ == "__main__":
    sol = Solver2015Day1()
    src = get_data(Solver2015Day1.YEAR, Solver2015Day1.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

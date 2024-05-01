from utils import Solver, get_data


class Solver2016Day18(Solver):
    YEAR = 2016
    DAY = 18

    def parse(self, src):
        return [int(ch == '^') for ch in src.strip()]

    def solve_part_1(self, src):
        ls = self.parse(src)
        m = len(ls)
        n = 40
        ls = [0] + ls + [0]
        ans = m - sum(ls)
        for _ in range(n - 1):
            ls = [0] + [int(sum(ls[i - 1:i + 2]) == 2 and ls[i] == 1 or
                            sum(ls[i - 1:i + 2]) == 1 and ls[i] == 0) for i in range(1, m + 1)] + [0]
            ans += m - sum(ls)
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        m = len(ls)
        n = 400000
        ls = [0] + ls + [0]
        ans = m - sum(ls)
        for _ in range(n - 1):
            ls = [0] + [int(sum(ls[i - 1:i + 2]) == 2 and ls[i] == 1 or
                            sum(ls[i - 1:i + 2]) == 1 and ls[i] == 0) for i in range(1, m + 1)] + [0]
            ans += m - sum(ls)
        return ans


if __name__ == "__main__":
    sol = Solver2016Day18()
    src = get_data(Solver2016Day18.YEAR, Solver2016Day18.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

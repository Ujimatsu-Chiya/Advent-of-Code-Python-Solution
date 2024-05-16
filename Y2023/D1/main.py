import re

from utils import Solver, get_data


class Solver2023Day1(Solver):
    YEAR = 2023
    DAY = 1

    def __init__(self, src):
        ls = src.strip().split()
        return ls

    def solve_part_1(self):
        inputs = self.parse(src)

        def cal(s):
            d = [ch for ch in s if ch.isdigit()]
            return int(d[0] + d[-1])

        ans = 0
        for s in inputs:
            ans += cal(s)
        return ans

    def solve_part_2(self):
        inputs = self.parse(src)
        ls = "one two three four five six seven eight nine".split()
        pat = re.compile("(?=(" + "|".join(ls) + "|\\d))")

        def cal(s):
            d = list(map(lambda t: str(ls.index(t) + 1) if t in ls else t, pat.findall(s)))
            return int(d[0] + d[-1])

        ans = 0
        for s in inputs:
            ans += cal(s)
        return ans


if __name__ == "__main__":
    sol = Solver2023Day1()
    src = get_data(Solver2023Day1.YEAR, Solver2023Day1.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

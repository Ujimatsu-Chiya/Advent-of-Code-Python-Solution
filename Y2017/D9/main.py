import re

from utils import Solver, get_data


class Solver2017Day9(Solver):
    YEAR = 2017
    DAY = 9

    def __init__(self, src):
        self.s = src.strip()

    def solve_part_1(self):
        s = self.s
        s = re.sub(r"!.", "", s)
        s = re.sub(r"<.*?>", "", s)
        ans = cnt = 0
        for ch in s:
            if ch == '{':
                cnt += 1
            elif ch == '}':
                ans += cnt
                cnt -= 1
        return ans

    def solve_part_2(self):
        s = self.s
        s = re.sub(r"!.", "", s)
        t = re.sub(r"<.*?>", "<>", s)
        return len(s) - len(t)


if __name__ == "__main__":
    src = get_data(Solver2017Day9.YEAR, Solver2017Day9.DAY)
    sol = Solver2017Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

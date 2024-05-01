import re

from utils import Solver, get_data


class Solver2017Day9(Solver):
    YEAR = 2017
    DAY = 9

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
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

    def solve_part_2(self, src):
        s = self.parse(src)
        s = re.sub(r"!.", "", s)
        t = re.sub(r"<.*?>", "<>", s)
        return len(s) - len(t)


if __name__ == "__main__":
    sol = Solver2017Day9()
    src = get_data(Solver2017Day9.YEAR, Solver2017Day9.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

import re

from utils import Solver, get_data


class Solver2015Day11(Solver):
    YEAR = 2015
    DAY = 11

    def __init__(self, src):
        self.s = src.strip()
        self.ans1 = self.ans2 = None

    def _solve(self, s):
        match = re.search(r'[iol]', s)
        if match:
            i = match.start()
            t = s[:i] + chr(ord(s[i]) + 1) + 'a' * (len(s) - i - 1)
            s = t
        while True:
            s = re.sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1)) + 1) + len(x.group(2)) * "a", s)
            if ("i" in s or "o" in s or "l" in s) or \
                    (len(re.findall(r'([a-z])\1', s)) < 2) or \
                    (len([1 for x, y, z in zip(s, s[1:], s[2:])
                          if ord(z) - ord(y) == 1 and ord(y) - ord(x) == 1]) == 0):
                continue
            return s

    def run(self):
        self.ans1 = self._solve(self.s)
        self.ans2 = self._solve(self.ans1)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2015Day11.YEAR, Solver2015Day11.DAY)
    sol = Solver2015Day11(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())

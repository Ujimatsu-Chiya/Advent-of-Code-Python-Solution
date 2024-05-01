import re

from utils import Solver, get_data


class Solver2015Day11(Solver):
    YEAR = 2015
    DAY = 11

    def parse(self, src):
        return src.strip()

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

    def solve_part_1(self, src):
        s = self.parse(src)
        return self._solve(s)

    def solve_part_2(self, src):
        return self._solve(self.solve_part_1(src))


if __name__ == "__main__":
    sol = Solver2015Day11()
    src = get_data(Solver2015Day11.YEAR, Solver2015Day11.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

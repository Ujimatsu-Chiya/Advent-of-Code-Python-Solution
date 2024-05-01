import re

from utils import Solver, get_data


class Solver2016Day7(Solver):
    YEAR = 2016
    DAY = 7

    def parse(self, src):
        return src.strip().split()

    def _get(self, s):
        inside = re.findall(r'\[(.*?)\]', s)
        outside = re.sub(r'\[.*?\]', ' ', s).split()
        return inside, outside

    def solve_part_1(self, src):
        ls = self.parse(src)

        def ok(s):
            for i in range(len(s) - 3):
                if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
                    return True
            return False

        ans = 0
        for s in ls:
            inside, outside = self._get(s)
            if all(not ok(s) for s in inside) and any(ok(s) for s in outside):
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            inside, outside = self._get(s)
            ok = False
            for s in inside:
                for i in range(len(s) - 2):
                    if s[i] == s[i + 2] and s[i] != s[i + 1]:
                        t = s[i + 1] + s[i] + s[i + 1]
                        ok |= any(t in w for w in outside)
            ans += ok
        return ans


if __name__ == "__main__":
    sol = Solver2016Day7()
    src = get_data(Solver2016Day7.YEAR, Solver2016Day7.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

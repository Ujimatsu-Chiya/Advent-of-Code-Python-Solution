import re

from utils import Solver, get_data


class Solver2016Day9(Solver):
    YEAR = 2016
    DAY = 9

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        pat = re.compile(r"(\d+)")
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i) + 1
                num_chars, num_repeats = map(int, pat.findall(s[i:j]))
                ans += num_chars * num_repeats
                i = j + num_chars
            else:
                ans += 1
                i += 1
        return ans

    def solve_part_2(self, src):
        s = self.parse(src)
        pat = re.compile(r"(\d+)")

        def dfs(s):
            ans = 0
            i = 0
            while i < len(s):
                if s[i] == '(':
                    j = s.find(')', i) + 1
                    num_chars, num_repeats = map(int, pat.findall(s[i:j]))
                    ans += num_repeats * dfs(s[j:j + num_chars])
                    i = j + num_chars
                else:
                    ans += 1
                    i += 1
            return ans

        return dfs(s)


if __name__ == "__main__":
    sol = Solver2016Day9()
    src = get_data(Solver2016Day9.YEAR, Solver2016Day9.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

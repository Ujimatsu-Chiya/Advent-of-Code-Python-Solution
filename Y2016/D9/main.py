import re

from utils import Solver, get_data


class Solver2016Day9(Solver):
    YEAR = 2016
    DAY = 9
    pat = re.compile(r"(\d+)")

    def __init__(self, src):
        self.s = src.strip()

    def solve_part_1(self):

        i = 0
        ans = 0
        while i < len(self.s):
            if self.s[i] == '(':
                j = self.s.find(')', i) + 1
                num_chars, num_repeats = map(int, self.pat.findall(self.s[i:j]))
                ans += num_chars * num_repeats
                i = j + num_chars
            else:
                ans += 1
                i += 1
        return ans

    def solve_part_2(self):
        def dfs(s):
            ans = 0
            i = 0
            while i < len(s):
                if s[i] == '(':
                    j = s.find(')', i) + 1
                    num_chars, num_repeats = map(int, self.pat.findall(s[i:j]))
                    ans += num_repeats * dfs(s[j:j + num_chars])
                    i = j + num_chars
                else:
                    ans += 1
                    i += 1
            return ans

        return dfs(self.s)


if __name__ == "__main__":
    src = get_data(Solver2016Day9.YEAR, Solver2016Day9.DAY)
    sol = Solver2016Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

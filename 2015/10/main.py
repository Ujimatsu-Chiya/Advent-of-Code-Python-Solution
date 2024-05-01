from utils import Solver, get_data


class Solver2015Day10(Solver):
    YEAR = 2015
    DAY = 10

    def parse(self, src):
        return src.strip()

    def _solve(self, s):
        ls = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            ls += [str(j - i), s[i]]
            i = j
        return ''.join(ls)

    def solve_part_1(self, src):
        s = self.parse(src)
        for i in range(40):
            s = self._solve(s)
        return len(s)

    def solve_part_2(self, src):
        s = self.parse(src)
        for i in range(50):
            s = self._solve(s)
        return len(s)


if __name__ == "__main__":
    sol = Solver2015Day10()
    src = get_data(Solver2015Day10.YEAR, Solver2015Day10.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

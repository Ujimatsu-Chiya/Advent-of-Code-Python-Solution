from utils import Solver, get_data


class Solver2015Day10(Solver):
    YEAR = 2015
    DAY = 10

    def __init__(self, src):
        self.s = src.strip()
        self.ans1 = self.ans2 = None

    def _trans(self, s):
        ls = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            ls += [str(j - i), s[i]]
            i = j
        return ''.join(ls)

    def _solve(self, s, k):
        for _ in range(k):
            s = self._trans(s)
        return s

    def solve_part_1(self):
        return len(self._solve(self.s, 40))

    def solve_part_2(self):
        return len(self._solve(self.s, 50))


if __name__ == "__main__":
    src = get_data(Solver2015Day10.YEAR, Solver2015Day10.DAY)
    sol = Solver2015Day10(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

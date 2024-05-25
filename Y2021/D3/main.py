from utils import Solver, get_data


class Solver2021Day3(Solver):
    YEAR = 2021
    DAY = 3

    def __init__(self, src):
        self.queries = src.strip().split()

    def solve_part_1(self):
        a = [[int(x) for x in u] for u in list(zip(*self.queries))]
        va = vb = 0
        for i, v in enumerate(a[::-1]):
            if v.count(1) > v.count(0):
                va |= 1 << i
            else:
                vb |= 1 << i
        return va * vb

    def solve_part_2(self):
        def solve(a, default, lt_flag):
            for j in range(len(a[0])):
                v = [s[j] for s in a]
                if v.count('1') == v.count('0'):
                    ch = default
                else:
                    ch = '1' if (v.count('1') > v.count('0')) ^ lt_flag else '0'
                a = [s for s in a if s[j] == ch]
                if len(a) == 1:
                    break
            return int(a[0], 2)

        return solve(self.queries, '1', False) * solve(self.queries, '0', True)


if __name__ == "__main__":
    src = get_data(Solver2021Day3.YEAR, Solver2021Day3.DAY)
    sol = Solver2021Day3(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

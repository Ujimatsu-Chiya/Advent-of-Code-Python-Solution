from utils import Solver, get_data


class Solver2015Day8(Solver):
    YEAR = 2015
    DAY = 8

    def __init__(self, src):
        self.queries = src.strip().split('\n')

    def solve_part_1(self):
        ans = 0
        for s in self.queries:
            ans += len(s) - len(eval(s))
        return ans

    def solve_part_2(self):
        ans = 0
        lt = str(self.queries).strip('[]').replace(r'"', r'\"').split(', ')
        for s, t in zip(self.queries, lt):
            ans += len(t) - len(s)
        return ans


if __name__ == "__main__":
    src = get_data(Solver2015Day8.YEAR, Solver2015Day8.DAY)
    sol = Solver2015Day8(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

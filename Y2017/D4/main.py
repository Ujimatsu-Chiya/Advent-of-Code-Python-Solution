from utils import Solver, get_data


class Solver2017Day4(Solver):
    YEAR = 2017
    DAY = 4

    def __init__(self, src):
        self.queries = [s.split() for s in src.strip().split('\n')]

    def solve_part_1(self):
        return len([1 for v in self.queries if len(v) == len(set(v))])

    def solve_part_2(self):
        ans = 0
        for v in self.queries:
            v = list(map(lambda s: "".join((lambda x: (x.sort(), x)[1])(list(s))), v))
            if len(v) == len(set(v)):
                ans += 1
        return ans


if __name__ == "__main__":
    src = get_data(Solver2017Day4.YEAR, Solver2017Day4.DAY)
    sol = Solver2017Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

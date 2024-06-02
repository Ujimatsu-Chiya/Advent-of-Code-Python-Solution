from utils import Solver, get_data
from functools import cmp_to_key
from itertools import chain


class Solver2022Day13(Solver):
    YEAR = 2022
    DAY = 13

    def __init__(self, src):
        self.queries = [[eval(s) for s in tmp.split('\n')] for tmp in src.strip().split('\n\n')]

    def compare(self, l0, l1):
        if isinstance(l0, int) and isinstance(l1, int):
            return -1 if l0 < l1 else 0 if l0 == l1 else 1
        elif isinstance(l0, int) and isinstance(l1, list):
            return self.compare([l0], l1)
        elif isinstance(l0, list) and isinstance(l1, int):
            return self.compare(l0, [l1])
        else:
            for v0, v1 in zip(l0, l1):
                x = self.compare(v0, v1)
                if x != 0:
                    return x
            return -1 if len(l0) < len(l1) else 0 if len(l0) == len(l1) else 1

    def solve_part_1(self):
        return sum(i + 1 for i, l in enumerate(self.queries) if self.compare(l[0], l[1]) <= 0)

    def solve_part_2(self):
        p1, p2 = [[2]], [[6]]
        a = sorted(list(chain.from_iterable(self.queries)) + [p1, p2], key=cmp_to_key(self.compare))
        return (a.index(p1) + 1) * (a.index(p2) + 1)


if __name__ == "__main__":
    src = get_data(Solver2022Day13.YEAR, Solver2022Day13.DAY)
    sol = Solver2022Day13(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())

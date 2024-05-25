from utils import Solver, get_data
from functools import reduce
from itertools import permutations

class Solver2021Day18(Solver):
    YEAR = 2021
    DAY = 18

    def __init__(self, src):
        self.queries = [eval(s) for s in src.strip().split()]

    def to_left(self, x, n):
        if n is None:
            return x
        if isinstance(x, int):
            return x + n
        return [self.to_left(x[0], n), x[1]]

    def to_right(self, x, n):
        if n is None:
            return x
        if isinstance(x, int):
            return x + n
        return [x[0], self.to_right(x[1], n)]

    def explode(self, x, dep):
        if isinstance(x, int):
            return False, None, x, None
        if dep == 0:
            return True, x[0], 0, x[1]
        u, v = x
        flag, left, u, right = self.explode(u, dep - 1)
        if flag:
            return True, left, [u, self.to_left(v, right)], None
        flag, left, v, right = self.explode(v, dep - 1)
        if flag:
            return True, None, [self.to_right(u, left), v], right
        return False, None, x, None

    def split(self, x):
        if isinstance(x, int):
            if x >= 10:
                return True, [x // 2, x - x // 2]
            return False, x
        u, v = x
        flag, u = self.split(u)
        if flag:
            return True, [u, v]
        flag, v = self.split(v)
        return flag, [u, v]

    def add(self, la, lb):
        ls = [la, lb]
        while True:
            flag, _, ls, _ = self.explode(ls, 4)
            if flag:
                continue
            flag, ls = self.split(ls)
            if not flag:
                break
        return ls

    def cal_value(self, a):
        if isinstance(a, int):
            return a
        else:
            return self.cal_value(a[0]) * 3 + self.cal_value(a[1]) * 2

    def solve_part_1(self):
        return self.cal_value(reduce(self.add, self.queries))

    def solve_part_2(self):
        return max(self.cal_value(self.add(*per)) for per in permutations(self.queries, 2))


if __name__ == "__main__":
    src = get_data(Solver2021Day18.YEAR, Solver2021Day18.DAY)
    sol = Solver2021Day18(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
